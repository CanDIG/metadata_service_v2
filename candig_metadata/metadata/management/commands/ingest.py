import json
import re
from uuid import uuid4
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from candig_metadata.metadata.models import Patient, Sample


CAMEL_CASE_PATTERN = re.compile(r'(?<!^)(?=[A-Z])')


def json_to_model(fields, row, obj):
    for field_name in fields:
        snake_case_field_name = CAMEL_CASE_PATTERN.sub('_', field_name).lower()

        if hasattr(obj, snake_case_field_name):
            setattr(obj, snake_case_field_name, row[field_name])
        else:
            print(f'Field {field_name} -> {snake_case_field_name} not found on {obj.__class__} model')


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

        with open(file_path) as json_file:
            data = json.load(json_file)

            for row in data['metadata']:
                if 'Patient' in row:
                    patient = Patient(dataset_id=dataset_id)
                    current_patient_id = row['Patient']['patientId']

                    fields = row['Patient'].keys()
                    json_to_model(row['Patient'].keys(), row['Patient'], patient)

                    patient.name = current_patient_id
                    patient.save()

                if 'Sample' in row:
                    sample = Sample(dataset_id=dataset_id)
                    fields = row['Sample'].keys()
                    json_to_model(row['Sample'].keys(), row['Sample'], sample)

                    sample.generate_name(current_patient_id)
                    sample.save()

                # TODO: Yup, import the other models also
                # TODO: Do not forget to generate the "name" field for these
