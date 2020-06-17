import json
import re
from uuid import uuid4
from pathlib import Path

from django.db import IntegrityError
from django.core.management.base import BaseCommand, CommandError

from candig_metadata.metadata.models import (
    Alignment,
    Celltransplant,
    Chemotherapy,
    Complication,
    Consent,
    Diagnosis,
    Enrollment,
    Expressionanalysis,
    Extraction,
    Fusiondetection,
    Immunotherapy,
    Labtest,
    Outcome,
    Patient,
    Sample,
    Radiotherapy,
    Sequencing,
    Slide,
    Study,
    Surgery,
    Tumourboard,
    Treatment,
    Variantcalling
)
from candig_metadata.metadata.backend import create_or_query_dataset


CAMEL_CASE_PATTERN = re.compile(r'(?<!^)(?=[A-Z])')


def json_to_model(fields, row, obj):
    empty = True

    for field_name in fields:
        snake_case_field_name = CAMEL_CASE_PATTERN.sub('_', field_name).lower()

        if hasattr(obj, snake_case_field_name):
            # May happens that every field provided are empty, do not save object then
            if snake_case_field_name[-4:] != 'tier' and row[field_name]:
                empty = False

            setattr(obj, snake_case_field_name, row[field_name])
        else:
            print(f'Field {field_name} -> {snake_case_field_name} not found on {obj.__class__} model')

    return not empty


class Command(BaseCommand):
    help = "Ingest metadata in JSON format for CanDIG"

    def add_arguments(self, parser):
        parser.add_argument(
            'dataset',
            type=str,
            help='The dataset ID'
        )
        parser.add_argument(
            'json_file',
            type=str,
            help='JSON File to ingest'
        )

    def handle(self, *args, **options):
        dataset_id = options['dataset']
        file_arg = options['json_file']

        file_path = Path(file_arg).resolve()

        if not file_path.exists():
            raise CommandError('JSON File provided does not exists')

        # TODO: query dataset service to confirm the ID exists?
        # dirty fix before connection to dataset service is done
        # dataset = Dataset.objects.get_or_create(id=dataset_id)
        if create_or_query_dataset(dataset_id):
            with open(file_path) as json_file:
                data = json.load(json_file)

                if 'metadata' in data:
                    for row in data['metadata']:
                        try:
                            if 'Patient' in row:
                                patient = Patient(id=uuid4(), dataset_id=dataset_id)
                                current_patient_id = row['Patient']['patientId']

                                json_to_model(row['Patient'].keys(), row['Patient'], patient)

                                patient.name = current_patient_id
                                patient.save()

                                print(f"Ingesting patient #{current_patient_id}")

                            if 'Sample' in row:
                                sample = Sample(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Sample'].keys(), row['Sample'], sample):
                                    sample.generate_name(current_patient_id)
                                    sample.save()

                                    print(f"Ingesting sample #{sample.name}")

                            if 'Celltransplant' in row:
                                celltransplant = Celltransplant(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Celltransplant'].keys(), row['Celltransplant'], celltransplant):
                                    celltransplant.generate_name(current_patient_id)
                                    celltransplant.save()

                                    print(f"Ingesting celltransplant #{celltransplant.name}")

                            if 'Chemotherapy' in row:
                                chemotherapy = Chemotherapy(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Chemotherapy'].keys(), row['Chemotherapy'], chemotherapy):
                                    chemotherapy.generate_name(current_patient_id)
                                    chemotherapy.save()

                                    print(f"Ingesting chemotherapy #{chemotherapy.name}")

                            if 'Complication' in row:
                                complication = Complication(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Complication'].keys(), row['Complication'], complication):
                                    complication.generate_name(current_patient_id)
                                    complication.save()

                                    print(f"Ingesting complication #{complication.name}")

                            if 'Consent' in row:
                                consent = Consent(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Consent'].keys(), row['Consent'], consent):
                                    consent.generate_name(current_patient_id)
                                    consent.save()

                                    print(f"Ingesting consent #{consent.name}")

                            if 'Diagnosis' in row:
                                diagnosis = Diagnosis(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Diagnosis'].keys(), row['Diagnosis'], diagnosis):
                                    diagnosis.generate_name(current_patient_id)
                                    diagnosis.save()

                                    print(f"Ingesting diagnosis #{diagnosis.name}")

                            if 'Enrollment' in row:
                                enrollment = Enrollment(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Enrollment'].keys(), row['Enrollment'], enrollment):
                                    enrollment.generate_name(current_patient_id)
                                    enrollment.save()

                                    print(f"Ingesting enrollment #{enrollment.name}")

                            if 'Immunotherapy' in row:
                                immunotherapy = Immunotherapy(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Immunotherapy'].keys(), row['Immunotherapy'], immunotherapy):
                                    immunotherapy.generate_name(current_patient_id)
                                    immunotherapy.save()

                                    print(f"Ingesting immunotherapy #{immunotherapy.name}")

                            if 'Labtest' in row:
                                labtest = Labtest(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Labtest'].keys(), row['Labtest'], labtest):
                                    labtest.generate_name(current_patient_id)
                                    labtest.save()

                                    print(f"Ingesting labtest #{labtest.name}")

                            if 'Outcome' in row:
                                outcome = Outcome(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Outcome'].keys(), row['Outcome'], outcome):
                                    outcome.generate_name(current_patient_id)
                                    outcome.save()

                                    print(f"Ingesting outcome #{outcome.name}")

                            if 'Radiotherapy' in row:
                                radiotherapy = Radiotherapy(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Radiotherapy'].keys(), row['Radiotherapy'], radiotherapy):
                                    radiotherapy.generate_name(current_patient_id)
                                    radiotherapy.save()

                                    print(f"Ingesting radiotherapy #{radiotherapy.name}")

                            if 'Slide' in row:
                                slide = Slide(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Slide'].keys(), row['Slide'], slide):
                                    slide.generate_name(current_patient_id)
                                    slide.save()

                                    print(f"Ingesting slide #{slide.name}")

                            if 'Study' in row:
                                study = Study(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Study'].keys(), row['Study'], study):
                                    study.generate_name(current_patient_id)
                                    study.save()

                                    print(f"Ingesting study #{study.name}")

                            if 'Surgery' in row:
                                surgery = Surgery(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Surgery'].keys(), row['Surgery'], surgery):
                                    surgery.generate_name(current_patient_id)
                                    surgery.save()

                                    print(f"Ingesting surgery #{surgery.name}")

                            if 'Tumourboard' in row:
                                tumourboard = Tumourboard(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Tumourboard'].keys(), row['Tumourboard'], tumourboard):
                                    tumourboard.generate_name(current_patient_id)
                                    tumourboard.save()

                                    print(f"Ingesting tumourboard #{tumourboard.name}")

                            if 'Treatment' in row:
                                treatment = Treatment(id=uuid4(), dataset_id=dataset_id)

                                if json_to_model(row['Treatment'].keys(), row['Treatment'], treatment):
                                    treatment.generate_name(current_patient_id)
                                    treatment.save()

                                    print(f"Ingesting complication #{complication.name}")

                        except IntegrityError:
                            if 'Patient' in row:
                                print(f"Duplicate entry for patient {row['Patient']['PatientId']}")
                            else:
                                print("Duplicate entry but no patient found")

                if 'pipeline_metadata' in data:
                    for row in data['pipeline_metadata']:
                        if 'Alignment' in row:
                            alignment = Alignment(id=uuid4(), dataset_id=dataset_id)

                            if json_to_model(row['Alignment'].keys(), row['Alignment'], alignment):
                                alignment.generate_name()
                                alignment.save()

                                print(f"Ingesting alignment #{alignment.name}")

                        if 'Expressionanalysis' in row:
                            expression_analysis = Expressionanalysis(id=uuid4(), dataset_id=dataset_id)

                            if json_to_model(row['Expressionanalysis'].keys(), row['Expressionanalysis'], expression_analysis):
                                expression_analysis.generate_name()
                                expression_analysis.save()

                                print(f"Ingesting expression_analysis #{expression_analysis.name}")

                        if 'Extraction' in row:
                            extraction = Extraction(id=uuid4(), dataset_id=dataset_id)

                            if json_to_model(row['Extraction'].keys(), row['Extraction'], extraction):
                                extraction.generate_name()
                                extraction.save()

                                print(f"Ingesting extraction #{extraction.name}")

                        if 'Fusiondetection' in row:
                            fusion_detection = Fusiondetection(id=uuid4(), dataset_id=dataset_id)

                            if json_to_model(row['Fusiondetection'].keys(), row['Fusiondetection'], fusion_detection):
                                fusion_detection.generate_name()
                                fusion_detection.save()

                                print(f"Ingesting fusion_detection #{fusion_detection.name}")

                        if 'Sequencing' in row:
                            sequencing = Sequencing(id=uuid4(), dataset_id=dataset_id)

                            if json_to_model(row['Sequencing'].keys(), row['Sequencing'], sequencing):
                                sequencing.generate_name()
                                sequencing.save()

                                print(f"Ingesting sequencing #{sequencing.name}")

                        if 'Variantcalling' in row:
                            variant_calling = Variantcalling(id=uuid4(), dataset_id=dataset_id)

                            if json_to_model(row['Variantcalling'].keys(), row['Variantcalling'], variant_calling):
                                variant_calling.generate_name()
                                variant_calling.save()

                                print(f"Ingesting variant_calling #{variant_calling.name}")
