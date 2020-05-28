import graphene
# TODO: which DjangoObjectType to use, from graphene_django or this one?
from graphene_django_extras.types import DjangoObjectType
from graphene_django.utils import (
    maybe_queryset,
    is_valid_django_model
)
from graphene_django_extras import DjangoFilterListField

from candig_metadata.metadata.models import (
    Chemotherapy,
    Complication,
    Consent,
    Diagnosis,
    Patient,
    Sample,
    Sequencing,
    Surgery
)
from candig_metadata.metadata.utils import resolve_field_factory


# TODO: use relay query format or not?
# Pros: May enable nested filters more easily
# Cons: The syntax is ugly
#class PatientNode(DjangoObjectType):
#    class Meta:
#        model = Patient
#        interfaces = (Node,)
#        filter_fields = ['patient_id']


class ChemotherapyType(DjangoObjectType):
    class Meta:
        model = Chemotherapy


class ComplicationType(DjangoObjectType):
    class Meta:
        model = Complication


class ConsentType(DjangoObjectType):
    class Meta:
        model = Consent


class DiagnosisType(DjangoObjectType):
    class Meta:
        model = Diagnosis


class SampleType(DjangoObjectType):
    class Meta:
        model = Sample
        filter_fields = {
            "sample_id": ("exact",),
            "sample_type": ("icontains", "iexact")
        }


class PatientType(DjangoObjectType):
    class Meta:
        model = Patient
        # TODO: Subclass and automatize?
        exclude_fields = []
        filter_fields = {
            "patient_id": ("exact",),
            "gender": ("exact",),
            "name": ("icontains", "iexact")
        }

    chemotherapies = graphene.List(ChemotherapyType)
    complications = graphene.List(ComplicationType)
    consents = graphene.List(ConsentType)
    samples = graphene.List(SampleType)

    def resolve_chemotherapies(self, info):
        return self.chemotherapy_set.all()

    def resolve_complications(self, info):
        return self.complication_set.all()

    def resolve_consents(self, info):
        return self.consent_set.all()

    def resolve_samples(self, info):
        return self.sample_set.all()


class SequencingType(DjangoObjectType):
    class Meta:
        model = Sequencing


class SurgeryType(DjangoObjectType):
    class Meta:
        model = Surgery


GRAPHQL_OBJECTS = [PatientType]


def apply_field_level_authorization():
    """
    For every GraphQL object we are exposing, check every fields of the model
    to see if there is a sibling {field_name}_tier (which indicates the access
    level necessary to read the file) and provide a resolve_field_name method
    on the object class to enforce, on the fly, this authorization rule.

    TODO: What about excluded fields (should not show these *_tier fields
    outside of the application but need these for what we are doing here.
    """
    for graphql_object in GRAPHQL_OBJECTS:
        fields = graphql_object._meta.fields

        for field in fields:
            tiered_field_name = f"{field}_tier"

            if tiered_field_name in fields:
                setattr(graphql_object, f"resolve_{field}", resolve_field_factory(field))


apply_field_level_authorization()


class Query:
    chemotherapies = DjangoFilterListField(ChemotherapyType)
    complications = DjangoFilterListField(ComplicationType)
    consents = DjangoFilterListField(ConsentType)
    diagnosis = DjangoFilterListField(DiagnosisType)
    patients = DjangoFilterListField(PatientType)
    samples = DjangoFilterListField(SampleType)
    sequencing = DjangoFilterListField(SequencingType)
    surgery = DjangoFilterListField(SurgeryType)
