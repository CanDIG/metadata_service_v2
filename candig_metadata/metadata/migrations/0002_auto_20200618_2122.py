# Generated by Django 3.0.7 on 2020-06-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='outcome',
            name='date_of_diagnosis_of_treatment_induced_neoplasm',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='date_of_diagnosis_of_treatment_induced_neoplasm_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='interval_progression_or_recurrence',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='interval_progression_or_recurrence_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='interval_regression_or_decrease_in_disease',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='interval_regression_or_decrease_in_disease_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='level_of_malignancy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='level_of_malignancy_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='site_of_relapse_or_progression',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='site_of_relapse_or_progression_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='treatment_induced_neoplasm_site',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='treatment_induced_neoplasm_site_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='actionable_expression_outlier',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='actionable_expression_outlier_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='actionable_germline_variant',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='actionable_germline_variant_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='actionable_somatic_variants',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='actionable_somatic_variants_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='any_actionable_expression_outlier',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='any_actionable_expression_outlier_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='any_actionable_germline_variants',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='any_actionable_germline_variants_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='any_actionable_somatic_variants',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='any_actionable_somatic_variants_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_altered_gene',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_altered_gene_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_drug',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_drug_class',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_drug_class_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_drug_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_non_actionable_gene',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_non_actionable_gene_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_type_of_alteration',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_type_of_alteration_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_type_of_analysis_used',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_type_of_analysis_used_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_type_of_information_utility',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='expression_type_of_information_utility_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='germline_variants_classification_of_variants',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='germline_variants_classification_of_variants_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='germline_variants_discussed',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='germline_variants_discussed_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='germline_variants_drug',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='germline_variants_drug_class',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='germline_variants_drug_class_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='germline_variants_drug_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='germline_variants_type_of_analysis_used',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='germline_variants_type_of_analysis_used_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='germline_variants_type_of_information_utility',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='germline_variants_type_of_information_utility_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='somatic_variants_discussed',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='somatic_variants_discussed_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='somatic_variants_drug',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='somatic_variants_drug_class',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='somatic_variants_drug_class_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='somatic_variants_drug_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='somatic_variants_non_actionable',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='somatic_variants_non_actionable_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='somatic_variants_type_of_analysis_used',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='somatic_variants_type_of_analysis_used_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='somatic_variants_type_of_information_utility',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tumourboard',
            name='somatic_variants_type_of_information_utility_tier',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]