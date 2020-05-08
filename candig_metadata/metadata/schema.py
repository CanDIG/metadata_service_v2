import graphene
from graphene import Node
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from graphene_django_extras import DjangoFilterListField

from candig_metadata.metadata.models import (
    Diagnosis,
    Patient,
    Sample,
    SampleURL,
    Sequencing,
    Surgery
)


# TODO: use relay query format or not?
# Pros: May enable nested filters more easily
# Cons: The syntax is ugly
#class PatientNode(DjangoObjectType):
#    class Meta:
#        model = Patient
#        interfaces = (Node,)
#        filter_fields = ['patient_id']


class DiagnosisType(DjangoObjectType):
    class Meta:
        model = Diagnosis


class PatientType(DjangoObjectType):
    class Meta:
        model = Patient
        filter_fields = {
            "patient_id": ("exact",),
            "gender": ("exact",),
            "name": ("icontains", "iexact")
        }


class SampleType(DjangoObjectType):
    class Meta:
        model = Sample
        filter_fields = {
            "sample_id": ("exact",),
            "sample_type": ("icontains", "iexact")
        }


class SampleURLType(DjangoObjectType):
    class Meta:
        model = SampleURL


class SequencingType(DjangoObjectType):
    class Meta:
        model = Sequencing


class SurgeryType(DjangoObjectType):
    class Meta:
        model = Surgery


class Query:
    all_diagnosis = DjangoFilterListField(DiagnosisType)
    all_patients = DjangoFilterListField(PatientType)
    all_samples = DjangoFilterListField(SampleType)
    all_sequencing = DjangoFilterListField(SequencingType)
    all_surgery = DjangoFilterListField(SurgeryType)
