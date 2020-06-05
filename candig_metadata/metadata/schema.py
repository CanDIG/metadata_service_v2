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
    Enrollment,
    Immunotherapy,
    Labtest,
    Outcome,
    Patient,
    Sample,
    Radiotherapy,
    Slide,
    Study,
    Surgery,
    Tumourboard,
    Treatment
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


class EnrollmentType(DjangoObjectType):
    class Meta:
        model = Enrollment


class ImmunotherapyType(DjangoObjectType):
    class Meta:
        model = Immunotherapy


class LabtestType(DjangoObjectType):
    class Meta:
        model = Labtest


class OutcomeType(DjangoObjectType):
    class Meta:
        model = Outcome


class SampleType(DjangoObjectType):
    class Meta:
        model = Sample
        filter_fields = {
            "sample_id": ("exact",),
            "sample_type": ("icontains", "iexact")
        }


class RadiotherapyType(DjangoObjectType):
    class Meta:
        model = Radiotherapy


class SlideType(DjangoObjectType):
    class Meta:
        model = Slide


class StudyType(DjangoObjectType):
    class Meta:
        model = Study


class SurgeryType(DjangoObjectType):
    class Meta:
        model = Surgery


class TreatmentType(DjangoObjectType):
    class Meta:
        model = Treatment


class TumourboardType(DjangoObjectType):
    class Meta:
        model = Tumourboard


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

    # These let use relationship in the style of GraphQL instead
    # of Django's
    # sample_set -> samples
    chemotherapies = graphene.List(ChemotherapyType)
    complications = graphene.List(ComplicationType)
    consents = graphene.List(ConsentType)
    diagnoses = graphene.List(DiagnosisType)
    enrollments = graphene.List(EnrollmentType)
    immunotherapies = graphene.List(ImmunotherapyType)
    labtests = graphene.List(LabtestType)
    outcomes = graphene.List(OutcomeType)
    radiotherapies = graphene.List(RadiotherapyType)
    samples = graphene.List(SampleType)
    slides = graphene.List(SlideType)
    studies = graphene.List(StudyType)
    surgeries = graphene.List(SurgeryType)
    treatments = graphene.List(TreatmentType)
    tumourboards = graphene.List(TumourboardType)

    def resolve_chemotherapies(self, info):
        return self.chemotherapy_set.all()

    def resolve_complications(self, info):
        return self.complication_set.all()

    def resolve_consents(self, info):
        return self.consent_set.all()

    def resolve_diagnoses(self, info):
        return self.diagnosis_set.all()

    def resolve_enrollments(self, info):
        return self.enrollment_set.all()

    def resolve_immunotherapies(self, info):
        return self.immunotherapy_set.all()

    def resolve_labtests(self, info):
        return self.labtest_set.all()

    def resolve_outcomes(self, info):
        return self.outcome_set.all()

    def resolve_radiotherapies(self, info):
        return self.radiotherapy_set.all()

    def resolve_samples(self, info):
        return self.sample_set.all()

    def resolve_slides(self, info):
        return self.slide_set.all()

    def resolve_studies(self, info):
        return self.study_set.all()

    def resolve_surgeries(self, info):
        return self.surgery_set.all()

    def resolve_treatments(self, info):
        return self.treatment_set.all()

    def resolve_tumourboards(self, info):
        return self.tumourboard_set.all()


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
    diagnoses = DjangoFilterListField(DiagnosisType)
    enrollments = DjangoFilterListField(EnrollmentType)
    immunotherapies = DjangoFilterListField(ImmunotherapyType)
    labtests = DjangoFilterListField(LabtestType)
    outcomes = DjangoFilterListField(OutcomeType)
    patients = DjangoFilterListField(PatientType)
    radiotherapies = DjangoFilterListField(RadiotherapyType)
    samples = DjangoFilterListField(SampleType)
    slides = DjangoFilterListField(SlideType)
    studies = DjangoFilterListField(StudyType)
    surgeries = DjangoFilterListField(SurgeryType)
    treatments = DjangoFilterListField(TreatmentType)
    tumourboards = DjangoFilterListField(TumourboardType)
