# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alignment(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey('Dataset', models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    alignment_id = models.TextField(db_column='alignmentId', blank=True, null=True)
    alignment_id_tier = models.IntegerField(db_column='alignmentIdTier', blank=True, null=True)
    sample_id = models.TextField(db_column='sampleId', blank=True, null=True)
    sample_id_tier = models.IntegerField(db_column='sampleIdTier', blank=True, null=True)
    in_house_pipeline = models.TextField(db_column='inHousePipeline', blank=True, null=True)
    in_house_pipeline_tier = models.IntegerField(db_column='inHousePipelineTier', blank=True, null=True)
    alignment_tool = models.TextField(db_column='alignmentTool', blank=True, null=True)
    alignment_tool_tier = models.IntegerField(db_column='alignmentToolTier', blank=True, null=True)
    merge_tool = models.TextField(db_column='mergeTool', blank=True, null=True)
    merge_tool_tier = models.IntegerField(db_column='mergeToolTier', blank=True, null=True)
    mark_duplicates = models.TextField(db_column='markDuplicates', blank=True, null=True)
    mark_duplicates_tier = models.IntegerField(db_column='markDuplicatesTier', blank=True, null=True)
    realigner_target = models.TextField(db_column='realignerTarget', blank=True, null=True)
    realigner_target_tier = models.IntegerField(db_column='realignerTargetTier', blank=True, null=True)
    indel_realigner = models.TextField(db_column='indelRealigner', blank=True, null=True)
    indel_realigner_tier = models.IntegerField(db_column='indelRealignerTier', blank=True, null=True)
    base_recalibrator = models.TextField(db_column='baseRecalibrator', blank=True, null=True)
    base_recalibrator_tier = models.IntegerField(db_column='baseRecalibratorTier', blank=True, null=True)
    print_reads = models.TextField(db_column='printReads', blank=True, null=True)
    print_reads_tier = models.IntegerField(db_column='printReadsTier', blank=True, null=True)
    idx_stats = models.TextField(db_column='idxStats', blank=True, null=True)
    idx_stats_tier = models.IntegerField(db_column='idxStatsTier', blank=True, null=True)
    flag_stat = models.TextField(db_column='flagStat', blank=True, null=True)
    flag_stat_tier = models.IntegerField(db_column='flagStatTier', blank=True, null=True)
    coverage = models.TextField(blank=True, null=True)
    coverage_tier = models.IntegerField(db_column='coverageTier', blank=True, null=True)
    insert_size_metrics = models.TextField(db_column='insertSizeMetrics', blank=True, null=True)
    insert_size_metrics_tier = models.IntegerField(db_column='insertSizeMetricsTier', blank=True, null=True)
    fastqc = models.TextField(blank=True, null=True)
    fastqc_tier = models.IntegerField(db_column='fastqcTier', blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    reference_tier = models.IntegerField(db_column='referenceTier', blank=True, null=True)
    sequencing_id = models.TextField(db_column='sequencingId', blank=True, null=True)
    sequencing_id_tier = models.IntegerField(db_column='sequencingIdTier', blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    site_tier = models.IntegerField(db_column='siteTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alignment'
        unique_together = (('dataset', 'name'),)


class Celltransplant(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey('Dataset', models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    start_date = models.TextField(db_column='startDate', blank=True, null=True)
    start_date_tier = models.IntegerField(db_column='startDateTier', blank=True, null=True)
    cell_source = models.TextField(db_column='cellSource', blank=True, null=True)
    cell_source_tier = models.IntegerField(db_column='cellSourceTier', blank=True, null=True)
    donor_type = models.TextField(db_column='donorType', blank=True, null=True)
    donor_type_tier = models.IntegerField(db_column='donorTypeTier', blank=True, null=True)
    treatment_plan_id = models.TextField(db_column='treatmentPlanId', blank=True, null=True)
    treatment_plan_id_tier = models.IntegerField(db_column='treatmentPlanIdTier', blank=True, null=True)
    course_number = models.TextField(db_column='courseNumber', blank=True, null=True)
    course_number_tier = models.IntegerField(db_column='courseNumberTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'celltransplant'
        unique_together = (('dataset', 'name'),)


class Chemotherapy(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey('Dataset', models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    course_number = models.TextField(db_column='courseNumber', blank=True, null=True)
    course_number_tier = models.IntegerField(db_column='courseNumberTier', blank=True, null=True)
    start_date = models.TextField(db_column='startDate', blank=True, null=True)
    start_date_tier = models.IntegerField(db_column='startDateTier', blank=True, null=True)
    stop_date = models.TextField(db_column='stopDate', blank=True, null=True)
    stop_date_tier = models.IntegerField(db_column='stopDateTier', blank=True, null=True)
    systematic_therapy_agent_name = models.TextField(db_column='systematicTherapyAgentName', blank=True, null=True)
    systematic_therapy_agent_name_tier = models.IntegerField(db_column='systematicTherapyAgentNameTier', blank=True, null=True)
    route = models.TextField(blank=True, null=True)
    route_tier = models.IntegerField(db_column='routeTier', blank=True, null=True)
    dose = models.TextField(blank=True, null=True)
    dose_tier = models.IntegerField(db_column='doseTier', blank=True, null=True)
    dose_frequency = models.TextField(db_column='doseFrequency', blank=True, null=True)
    dose_frequency_tier = models.IntegerField(db_column='doseFrequencyTier', blank=True, null=True)
    dose_unit = models.TextField(db_column='doseUnit', blank=True, null=True)
    dose_unit_tier = models.IntegerField(db_column='doseUnitTier', blank=True, null=True)
    days_per_cycle = models.TextField(db_column='daysPerCycle', blank=True, null=True)
    days_per_cycle_tier = models.IntegerField(db_column='daysPerCycleTier', blank=True, null=True)
    number_of_cycle = models.TextField(db_column='numberOfCycle', blank=True, null=True)
    number_of_cycle_tier = models.IntegerField(db_column='numberOfCycleTier', blank=True, null=True)
    treatment_intent = models.TextField(db_column='treatmentIntent', blank=True, null=True)
    treatment_intent_tier = models.IntegerField(db_column='treatmentIntentTier', blank=True, null=True)
    treating_centre_name = models.TextField(db_column='treatingCentreName', blank=True, null=True)
    treating_centre_name_tier = models.IntegerField(db_column='treatingCentreNameTier', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    type_tier = models.IntegerField(db_column='typeTier', blank=True, null=True)
    protocol_code = models.TextField(db_column='protocolCode', blank=True, null=True)
    protocol_code_tier = models.IntegerField(db_column='protocolCodeTier', blank=True, null=True)
    recording_date = models.TextField(db_column='recordingDate', blank=True, null=True)
    recording_date_tier = models.IntegerField(db_column='recordingDateTier', blank=True, null=True)
    treatment_plan_id = models.TextField(db_column='treatmentPlanId', blank=True, null=True)
    treatment_plan_id_tier = models.IntegerField(db_column='treatmentPlanIdTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chemotherapy'
        unique_together = (('dataset', 'name'),)

    def generate_name(self, patient_id):
        self.name = f"{patient_id}_{self.treatment_plan_id}_{self.systematic_therapy_agent_name}"


class Complication(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey('Dataset', models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    date_tier = models.IntegerField(db_column='dateTier', blank=True, null=True)
    late_complication_of_therapy_developed = models.TextField(db_column='lateComplicationOfTherapyDeveloped', blank=True, null=True)
    late_complication_of_therapy_developed_tier = models.IntegerField(db_column='lateComplicationOfTherapyDevelopedTier', blank=True, null=True)
    late_toxicity_detail = models.TextField(db_column='lateToxicityDetail', blank=True, null=True)
    late_toxicity_detail_tier = models.IntegerField(db_column='lateToxicityDetailTier', blank=True, null=True)
    suspected_treatment_induced_neoplasm_developed = models.TextField(db_column='suspectedTreatmentInducedNeoplasmDeveloped', blank=True, null=True)
    suspected_treatment_induced_neoplasm_developed_tier = models.IntegerField(db_column='suspectedTreatmentInducedNeoplasmDevelopedTier', blank=True, null=True)
    treatment_induced_neoplasm_details = models.TextField(db_column='treatmentInducedNeoplasmDetails', blank=True, null=True)
    treatment_induced_neoplasm_details_tier = models.IntegerField(db_column='treatmentInducedNeoplasmDetailsTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complication'
        unique_together = (('dataset', 'name'),)

    def generate_name(self, patient_id):
        self.name = f"{patient_id}_{self.date}"


class Consent(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey('Dataset', models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    consent_id = models.TextField(db_column='consentId', blank=True, null=True)
    consent_id_tier = models.IntegerField(db_column='consentIdTier', blank=True, null=True)
    consent_date = models.TextField(db_column='consentDate', blank=True, null=True)
    consent_date_tier = models.IntegerField(db_column='consentDateTier', blank=True, null=True)
    consent_version = models.TextField(db_column='consentVersion', blank=True, null=True)
    consent_version_tier = models.IntegerField(db_column='consentVersionTier', blank=True, null=True)
    patient_consented_to = models.TextField(db_column='patientConsentedTo', blank=True, null=True)
    patient_consented_to_tier = models.IntegerField(db_column='patientConsentedToTier', blank=True, null=True)
    reason_for_rejection = models.TextField(db_column='reasonForRejection', blank=True, null=True)
    reason_for_rejection_tier = models.IntegerField(db_column='reasonForRejectionTier', blank=True, null=True)
    was_assent_obtained = models.TextField(db_column='wasAssentObtained', blank=True, null=True)
    was_assent_obtained_tier = models.IntegerField(db_column='wasAssentObtainedTier', blank=True, null=True)
    date_of_assent = models.TextField(db_column='dateOfAssent', blank=True, null=True)
    date_of_assent_tier = models.IntegerField(db_column='dateOfAssentTier', blank=True, null=True)
    assent_form_version = models.TextField(db_column='assentFormVersion', blank=True, null=True)
    assent_form_version_tier = models.IntegerField(db_column='assentFormVersionTier', blank=True, null=True)
    if_assent_not_obtained_why_not = models.TextField(db_column='ifAssentNotObtainedWhyNot', blank=True, null=True)
    if_assent_not_obtained_why_not_tier = models.IntegerField(db_column='ifAssentNotObtainedWhyNotTier', blank=True, null=True)
    reconsent_date = models.TextField(db_column='reconsentDate', blank=True, null=True)
    reconsent_date_tier = models.IntegerField(db_column='reconsentDateTier', blank=True, null=True)
    reconsent_version = models.TextField(db_column='reconsentVersion', blank=True, null=True)
    reconsent_version_tier = models.IntegerField(db_column='reconsentVersionTier', blank=True, null=True)
    consenting_coordinator_name = models.TextField(db_column='consentingCoordinatorName', blank=True, null=True)
    consenting_coordinator_name_tier = models.IntegerField(db_column='consentingCoordinatorNameTier', blank=True, null=True)
    previously_consented = models.TextField(db_column='previouslyConsented', blank=True, null=True)
    previously_consented_tier = models.IntegerField(db_column='previouslyConsentedTier', blank=True, null=True)
    name_of_other_biobank = models.TextField(db_column='nameOfOtherBiobank', blank=True, null=True)
    name_of_other_biobank_tier = models.IntegerField(db_column='nameOfOtherBiobankTier', blank=True, null=True)
    has_consent_been_withdrawn = models.TextField(db_column='hasConsentBeenWithdrawn', blank=True, null=True)
    has_consent_been_withdrawn_tier = models.IntegerField(db_column='hasConsentBeenWithdrawnTier', blank=True, null=True)
    date_of_consent_withdrawal = models.TextField(db_column='dateOfConsentWithdrawal', blank=True, null=True)
    date_of_consent_withdrawal_tier = models.IntegerField(db_column='dateOfConsentWithdrawalTier', blank=True, null=True)
    type_of_consent_withdrawal = models.TextField(db_column='typeOfConsentWithdrawal', blank=True, null=True)
    type_of_consent_withdrawal_tier = models.IntegerField(db_column='typeOfConsentWithdrawalTier', blank=True, null=True)
    reason_for_consent_withdrawal = models.TextField(db_column='reasonForConsentWithdrawal', blank=True, null=True)
    reason_for_consent_withdrawal_tier = models.IntegerField(db_column='reasonForConsentWithdrawalTier', blank=True, null=True)
    consent_form_complete = models.TextField(db_column='consentFormComplete', blank=True, null=True)
    consent_form_complete_tier = models.IntegerField(db_column='consentFormCompleteTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consent'
        unique_together = (('dataset', 'name'),)

    def generate_name(self, patient_id):
        self.name = f"{patient_id}_{self.consent_date}"

class Dataset(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'dataset'


class Diagnosis(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    diagnosis_id = models.TextField(db_column='diagnosisId', unique=True, blank=True, null=True)
    diagnosis_id_tier = models.IntegerField(db_column='diagnosisIdTier', blank=True, null=True)
    diagnosis_date = models.TextField(db_column='diagnosisDate', blank=True, null=True)
    diagnosis_date_tier = models.IntegerField(db_column='diagnosisDateTier', blank=True, null=True)
    age_at_diagnosis = models.TextField(db_column='ageAtDiagnosis', blank=True, null=True)
    age_at_diagnosis_tier = models.IntegerField(db_column='ageAtDiagnosisTier', blank=True, null=True)
    cancer_type = models.TextField(db_column='cancerType', blank=True, null=True)
    cancer_type_tier = models.IntegerField(db_column='cancerTypeTier', blank=True, null=True)
    classification = models.TextField(blank=True, null=True)
    classification_tier = models.IntegerField(db_column='classificationTier', blank=True, null=True)
    cancer_site = models.TextField(db_column='cancerSite', blank=True, null=True)
    cancer_site_tier = models.IntegerField(db_column='cancerSiteTier', blank=True, null=True)
    histology = models.TextField(blank=True, null=True)
    histology_tier = models.IntegerField(db_column='histologyTier', blank=True, null=True)
    method_of_definitive_diagnosis = models.TextField(db_column='methodOfDefinitiveDiagnosis', blank=True, null=True)
    method_of_definitive_diagnosis_tier = models.IntegerField(db_column='methodOfDefinitiveDiagnosisTier', blank=True, null=True)
    sample_type = models.TextField(db_column='sampleType', blank=True, null=True)
    sample_type_tier = models.IntegerField(db_column='sampleTypeTier', blank=True, null=True)
    sample_site = models.TextField(db_column='sampleSite', blank=True, null=True)
    sample_site_tier = models.IntegerField(db_column='sampleSiteTier', blank=True, null=True)
    tumor_grade = models.TextField(db_column='tumorGrade', blank=True, null=True)
    tumor_grade_tier = models.IntegerField(db_column='tumorGradeTier', blank=True, null=True)
    grading_system_used = models.TextField(db_column='gradingSystemUsed', blank=True, null=True)
    grading_system_used_tier = models.IntegerField(db_column='gradingSystemUsedTier', blank=True, null=True)
    sites_of_metastases = models.TextField(db_column='sitesOfMetastases', blank=True, null=True)
    sites_of_metastases_tier = models.IntegerField(db_column='sitesOfMetastasesTier', blank=True, null=True)
    staging_system = models.TextField(db_column='stagingSystem', blank=True, null=True)
    staging_system_tier = models.IntegerField(db_column='stagingSystemTier', blank=True, null=True)
    version_or_edition_of_the_staging_system = models.TextField(db_column='versionOrEditionOfTheStagingSystem', blank=True, null=True)
    version_or_edition_of_the_staging_system_tier = models.IntegerField(db_column='versionOrEditionOfTheStagingSystemTier', blank=True, null=True)
    specific_tumor_stage_at_diagnosis = models.TextField(db_column='specificTumorStageAtDiagnosis', blank=True, null=True)
    specific_tumor_stage_at_diagnosis_tier = models.IntegerField(db_column='specificTumorStageAtDiagnosisTier', blank=True, null=True)
    prognostic_biomarkers = models.TextField(db_column='prognosticBiomarkers', blank=True, null=True)
    prognostic_biomarkers_tier = models.IntegerField(db_column='prognosticBiomarkersTier', blank=True, null=True)
    biomarker_quantification = models.TextField(db_column='biomarkerQuantification', blank=True, null=True)
    biomarker_quantification_tier = models.IntegerField(db_column='biomarkerQuantificationTier', blank=True, null=True)
    additional_molecular_testing = models.TextField(db_column='additionalMolecularTesting', blank=True, null=True)
    additional_molecular_testing_tier = models.IntegerField(db_column='additionalMolecularTestingTier', blank=True, null=True)
    additional_test_type = models.TextField(db_column='additionalTestType', blank=True, null=True)
    additional_test_type_tier = models.IntegerField(db_column='additionalTestTypeTier', blank=True, null=True)
    laboratory_name = models.TextField(db_column='laboratoryName', blank=True, null=True)
    laboratory_name_tier = models.IntegerField(db_column='laboratoryNameTier', blank=True, null=True)
    laboratory_address = models.TextField(db_column='laboratoryAddress', blank=True, null=True)
    laboratory_address_tier = models.IntegerField(db_column='laboratoryAddressTier', blank=True, null=True)
    site_of_metastases = models.TextField(db_column='siteOfMetastases', blank=True, null=True)
    site_of_metastases_tier = models.IntegerField(db_column='siteOfMetastasesTier', blank=True, null=True)
    staging_system_version = models.TextField(db_column='stagingSystemVersion', blank=True, null=True)
    staging_system_version_tier = models.IntegerField(db_column='stagingSystemVersionTier', blank=True, null=True)
    specific_stage = models.TextField(db_column='specificStage', blank=True, null=True)
    specific_stage_tier = models.IntegerField(db_column='specificStageTier', blank=True, null=True)
    cancer_specific_biomarkers = models.TextField(db_column='cancerSpecificBiomarkers', blank=True, null=True)
    cancer_specific_biomarkers_tier = models.IntegerField(db_column='cancerSpecificBiomarkersTier', blank=True, null=True)
    additional_molecular_diagnostic_testing_performed = models.TextField(db_column='additionalMolecularDiagnosticTestingPerformed', blank=True, null=True)
    additional_molecular_diagnostic_testing_performed_tier = models.IntegerField(db_column='additionalMolecularDiagnosticTestingPerformedTier', blank=True, null=True)
    additional_test = models.TextField(db_column='additionalTest', blank=True, null=True)
    additional_test_tier = models.IntegerField(db_column='additionalTestTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diagnosis'
        unique_together = (('dataset', 'name'),)

    def generate_name(self, patient_id):
        self.name = f"{patient_id}_{self.diagnosis_date}"


class Enrollment(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    enrollment_institution = models.TextField(db_column='enrollmentInstitution', blank=True, null=True)
    enrollment_institution_tier = models.IntegerField(db_column='enrollmentInstitutionTier', blank=True, null=True)
    enrollment_approval_date = models.TextField(db_column='enrollmentApprovalDate', blank=True, null=True)
    enrollment_approval_date_tier = models.IntegerField(db_column='enrollmentApprovalDateTier', blank=True, null=True)
    cross_enrollment = models.TextField(db_column='crossEnrollment', blank=True, null=True)
    cross_enrollment_tier = models.IntegerField(db_column='crossEnrollmentTier', blank=True, null=True)
    other_personalized_medicine_study_name = models.TextField(db_column='otherPersonalizedMedicineStudyName', blank=True, null=True)
    other_personalized_medicine_study_name_tier = models.IntegerField(db_column='otherPersonalizedMedicineStudyNameTier', blank=True, null=True)
    other_personalized_medicine_study_id = models.TextField(db_column='otherPersonalizedMedicineStudyId', blank=True, null=True)
    other_personalized_medicine_study_id_tier = models.IntegerField(db_column='otherPersonalizedMedicineStudyIdTier', blank=True, null=True)
    age_at_enrollment = models.TextField(db_column='ageAtEnrollment', blank=True, null=True)
    age_at_enrollment_tier = models.IntegerField(db_column='ageAtEnrollmentTier', blank=True, null=True)
    eligibility_category = models.TextField(db_column='eligibilityCategory', blank=True, null=True)
    eligibility_category_tier = models.IntegerField(db_column='eligibilityCategoryTier', blank=True, null=True)
    status_at_enrollment = models.TextField(db_column='statusAtEnrollment', blank=True, null=True)
    status_at_enrollment_tier = models.IntegerField(db_column='statusAtEnrollmentTier', blank=True, null=True)
    primary_oncologist_name = models.TextField(db_column='primaryOncologistName', blank=True, null=True)
    primary_oncologist_name_tier = models.IntegerField(db_column='primaryOncologistNameTier', blank=True, null=True)
    primary_oncologist_contact = models.TextField(db_column='primaryOncologistContact', blank=True, null=True)
    primary_oncologist_contact_tier = models.IntegerField(db_column='primaryOncologistContactTier', blank=True, null=True)
    referring_physician_name = models.TextField(db_column='referringPhysicianName', blank=True, null=True)
    referring_physician_name_tier = models.IntegerField(db_column='referringPhysicianNameTier', blank=True, null=True)
    referring_physician_contact = models.TextField(db_column='referringPhysicianContact', blank=True, null=True)
    referring_physician_contact_tier = models.IntegerField(db_column='referringPhysicianContactTier', blank=True, null=True)
    summary_of_id_request = models.TextField(db_column='summaryOfIdRequest', blank=True, null=True)
    summary_of_id_request_tier = models.IntegerField(db_column='summaryOfIdRequestTier', blank=True, null=True)
    treating_centre_name = models.TextField(db_column='treatingCentreName', blank=True, null=True)
    treating_centre_name_tier = models.IntegerField(db_column='treatingCentreNameTier', blank=True, null=True)
    treating_centre_province = models.TextField(db_column='treatingCentreProvince', blank=True, null=True)
    treating_centre_province_tier = models.IntegerField(db_column='treatingCentreProvinceTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enrollment'
        unique_together = (('dataset', 'name'),)

    def generate_name(self, patient_id):
        self.name = f"{patient_id}_{self.enrollment_approval_date}"


class Expressionanalysis(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    expression_analysis_id = models.TextField(db_column='expressionAnalysisId', blank=True, null=True)
    expression_analysis_id_tier = models.IntegerField(db_column='expressionAnalysisIdTier', blank=True, null=True)
    sample_id = models.TextField(db_column='sampleId', blank=True, null=True)
    sample_id_tier = models.IntegerField(db_column='sampleIdTier', blank=True, null=True)
    read_length = models.TextField(db_column='readLength', blank=True, null=True)
    read_length_tier = models.IntegerField(db_column='readLengthTier', blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    reference_tier = models.IntegerField(db_column='referenceTier', blank=True, null=True)
    alignment_tool = models.TextField(db_column='alignmentTool', blank=True, null=True)
    alignment_tool_tier = models.IntegerField(db_column='alignmentToolTier', blank=True, null=True)
    bam_handling = models.TextField(db_column='bamHandling', blank=True, null=True)
    bam_handling_tier = models.IntegerField(db_column='bamHandlingTier', blank=True, null=True)
    expression_estimation = models.TextField(db_column='expressionEstimation', blank=True, null=True)
    expression_estimation_tier = models.IntegerField(db_column='expressionEstimationTier', blank=True, null=True)
    sequencing_id = models.TextField(db_column='sequencingId', blank=True, null=True)
    sequencing_id_tier = models.IntegerField(db_column='sequencingIdTier', blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    site_tier = models.IntegerField(db_column='siteTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expressionanalysis'
        unique_together = (('dataset', 'name'),)


class Extraction(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    extraction_id = models.TextField(db_column='extractionId', blank=True, null=True)
    extraction_id_tier = models.IntegerField(db_column='extractionIdTier', blank=True, null=True)
    sample_id = models.TextField(db_column='sampleId', blank=True, null=True)
    sample_id_tier = models.IntegerField(db_column='sampleIdTier', blank=True, null=True)
    rna_blood = models.TextField(db_column='rnaBlood', blank=True, null=True)
    rna_blood_tier = models.IntegerField(db_column='rnaBloodTier', blank=True, null=True)
    dna_blood = models.TextField(db_column='dnaBlood', blank=True, null=True)
    dna_blood_tier = models.IntegerField(db_column='dnaBloodTier', blank=True, null=True)
    rna_tissue = models.TextField(db_column='rnaTissue', blank=True, null=True)
    rna_tissue_tier = models.IntegerField(db_column='rnaTissueTier', blank=True, null=True)
    dna_tissue = models.TextField(db_column='dnaTissue', blank=True, null=True)
    dna_tissue_tier = models.IntegerField(db_column='dnaTissueTier', blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    site_tier = models.IntegerField(db_column='siteTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extraction'
        unique_together = (('dataset', 'name'),)


class Fusiondetection(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    fusion_detection_id = models.TextField(db_column='fusionDetectionId', blank=True, null=True)
    fusion_detection_id_tier = models.IntegerField(db_column='fusionDetectionIdTier', blank=True, null=True)
    sample_id = models.TextField(db_column='sampleId', blank=True, null=True)
    sample_id_tier = models.IntegerField(db_column='sampleIdTier', blank=True, null=True)
    in_house_pipeline = models.TextField(db_column='inHousePipeline', blank=True, null=True)
    in_house_pipeline_tier = models.IntegerField(db_column='inHousePipelineTier', blank=True, null=True)
    sv_detection = models.TextField(db_column='svDetection', blank=True, null=True)
    sv_detection_tier = models.IntegerField(db_column='svDetectionTier', blank=True, null=True)
    fusion_detection = models.TextField(db_column='fusionDetection', blank=True, null=True)
    fusion_detection_tier = models.IntegerField(db_column='fusionDetectionTier', blank=True, null=True)
    realignment = models.TextField(blank=True, null=True)
    realignment_tier = models.IntegerField(db_column='realignmentTier', blank=True, null=True)
    annotation = models.TextField(blank=True, null=True)
    annotation_tier = models.IntegerField(db_column='annotationTier', blank=True, null=True)
    genome_reference = models.TextField(db_column='genomeReference', blank=True, null=True)
    genome_reference_tier = models.IntegerField(db_column='genomeReferenceTier', blank=True, null=True)
    gene_models = models.TextField(db_column='geneModels', blank=True, null=True)
    gene_models_tier = models.IntegerField(db_column='geneModelsTier', blank=True, null=True)
    alignment_id = models.TextField(db_column='alignmentId', blank=True, null=True)
    alignment_id_tier = models.IntegerField(db_column='alignmentIdTier', blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    site_tier = models.IntegerField(db_column='siteTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fusiondetection'
        unique_together = (('dataset', 'name'),)


class Immunotherapy(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    start_date = models.TextField(db_column='startDate', blank=True, null=True)
    start_date_tier = models.IntegerField(db_column='startDateTier', blank=True, null=True)
    immunotherapy_type = models.TextField(db_column='immunotherapyType', blank=True, null=True)
    immunotherapy_type_tier = models.IntegerField(db_column='immunotherapyTypeTier', blank=True, null=True)
    immunotherapy_target = models.TextField(db_column='immunotherapyTarget', blank=True, null=True)
    immunotherapy_target_tier = models.IntegerField(db_column='immunotherapyTargetTier', blank=True, null=True)
    immunotherapy_detail = models.TextField(db_column='immunotherapyDetail', blank=True, null=True)
    immunotherapy_detail_tier = models.IntegerField(db_column='immunotherapyDetailTier', blank=True, null=True)
    treatment_plan_id = models.TextField(db_column='treatmentPlanId', blank=True, null=True)
    treatment_plan_id_tier = models.IntegerField(db_column='treatmentPlanIdTier', blank=True, null=True)
    course_number = models.TextField(db_column='courseNumber', blank=True, null=True)
    course_number_tier = models.IntegerField(db_column='courseNumberTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'immunotherapy'
        unique_together = (('dataset', 'name'),)


class Labtest(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    start_date = models.TextField(db_column='startDate', blank=True, null=True)
    start_date_tier = models.IntegerField(db_column='startDateTier', blank=True, null=True)
    collection_date = models.TextField(db_column='collectionDate', blank=True, null=True)
    collection_date_tier = models.IntegerField(db_column='collectionDateTier', blank=True, null=True)
    end_date = models.TextField(db_column='endDate', blank=True, null=True)
    end_date_tier = models.IntegerField(db_column='endDateTier', blank=True, null=True)
    event_type = models.TextField(db_column='eventType', blank=True, null=True)
    event_type_tier = models.IntegerField(db_column='eventTypeTier', blank=True, null=True)
    test_results = models.TextField(db_column='testResults', blank=True, null=True)
    test_results_tier = models.IntegerField(db_column='testResultsTier', blank=True, null=True)
    time_point = models.TextField(db_column='timePoint', blank=True, null=True)
    time_point_tier = models.IntegerField(db_column='timePointTier', blank=True, null=True)
    recording_date = models.TextField(db_column='recordingDate', blank=True, null=True)
    recording_date_tier = models.IntegerField(db_column='recordingDateTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labtest'
        unique_together = (('dataset', 'name'),)

    def generate_name(self, patient_id):
        self.name = f"{patient_id}_{self.start_date}"


class Outcome(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    physical_exam_id = models.TextField(db_column='physicalExamId', blank=True, null=True)
    physical_exam_id_tier = models.IntegerField(db_column='physicalExamIdTier', blank=True, null=True)
    date_of_assessment = models.TextField(db_column='dateOfAssessment', blank=True, null=True)
    date_of_assessment_tier = models.IntegerField(db_column='dateOfAssessmentTier', blank=True, null=True)
    disease_response_or_status = models.TextField(db_column='diseaseResponseOrStatus', blank=True, null=True)
    disease_response_or_status_tier = models.IntegerField(db_column='diseaseResponseOrStatusTier', blank=True, null=True)
    other_response_classification = models.TextField(db_column='otherResponseClassification', blank=True, null=True)
    other_response_classification_tier = models.IntegerField(db_column='otherResponseClassificationTier', blank=True, null=True)
    minimal_residual_disease_assessment = models.TextField(db_column='minimalResidualDiseaseAssessment', blank=True, null=True)
    minimal_residual_disease_assessment_tier = models.IntegerField(db_column='minimalResidualDiseaseAssessmentTier', blank=True, null=True)
    method_of_response_evaluation = models.TextField(db_column='methodOfResponseEvaluation', blank=True, null=True)
    method_of_response_evaluation_tier = models.IntegerField(db_column='methodOfResponseEvaluationTier', blank=True, null=True)
    response_criteria_used = models.TextField(db_column='responseCriteriaUsed', blank=True, null=True)
    response_criteria_used_tier = models.IntegerField(db_column='responseCriteriaUsedTier', blank=True, null=True)
    summary_stage = models.TextField(db_column='summaryStage', blank=True, null=True)
    summary_stage_tier = models.IntegerField(db_column='summaryStageTier', blank=True, null=True)
    sites_of_any_progression_or_recurrence = models.TextField(db_column='sitesOfAnyProgressionOrRecurrence', blank=True, null=True)
    sites_of_any_progression_or_recurrence_tier = models.IntegerField(db_column='sitesOfAnyProgressionOrRecurrenceTier', blank=True, null=True)
    vital_status = models.TextField(db_column='vitalStatus', blank=True, null=True)
    vital_status_tier = models.IntegerField(db_column='vitalStatusTier', blank=True, null=True)
    height = models.TextField(blank=True, null=True)
    height_tier = models.IntegerField(db_column='heightTier', blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    weight_tier = models.IntegerField(db_column='weightTier', blank=True, null=True)
    height_units = models.TextField(db_column='heightUnits', blank=True, null=True)
    height_units_tier = models.IntegerField(db_column='heightUnitsTier', blank=True, null=True)
    weight_units = models.TextField(db_column='weightUnits', blank=True, null=True)
    weight_units_tier = models.IntegerField(db_column='weightUnitsTier', blank=True, null=True)
    performance_status = models.TextField(db_column='performanceStatus', blank=True, null=True)
    performance_status_tier = models.IntegerField(db_column='performanceStatusTier', blank=True, null=True)
    overall_survival_in_months = models.TextField(db_column='overallSurvivalInMonths', blank=True, null=True)
    overall_survival_in_months_tier = models.IntegerField(db_column='overallSurvivalInMonthsTier', blank=True, null=True)
    disease_free_survival_in_months = models.TextField(db_column='diseaseFreeSurvivalInMonths', blank=True, null=True)
    disease_free_survival_in_months_tier = models.IntegerField(db_column='diseaseFreeSurvivalInMonthsTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outcome'
        unique_together = (('dataset', 'name'),)

    def generate_name(self, patient_id):
        self.name = f"{patient_id}_{self.date_of_assessment}"


class Patient(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True, unique=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    other_ids = models.TextField(db_column='otherIds', blank=True, null=True)
    other_ids_tier = models.IntegerField(db_column='otherIdsTier', blank=True, null=True)
    date_of_birth = models.TextField(db_column='dateOfBirth', blank=True, null=True)
    date_of_birth_tier = models.IntegerField(db_column='dateOfBirthTier', blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    gender_tier = models.IntegerField(db_column='genderTier', blank=True, null=True)
    ethnicity = models.TextField(blank=True, null=True)
    ethnicity_tier = models.IntegerField(db_column='ethnicityTier', blank=True, null=True)
    race = models.TextField(blank=True, null=True)
    race_tier = models.IntegerField(db_column='raceTier', blank=True, null=True)
    province_of_residence = models.TextField(db_column='provinceOfResidence', blank=True, null=True)
    province_of_residence_tier = models.IntegerField(db_column='provinceOfResidenceTier', blank=True, null=True)
    date_of_death = models.TextField(db_column='dateOfDeath', blank=True, null=True)
    date_of_death_tier = models.IntegerField(db_column='dateOfDeathTier', blank=True, null=True)
    cause_of_death = models.TextField(db_column='causeOfDeath', blank=True, null=True)
    cause_of_death_tier = models.IntegerField(db_column='causeOfDeathTier', blank=True, null=True)
    autopsy_tissue_for_research = models.TextField(db_column='autopsyTissueForResearch', blank=True, null=True)
    autopsy_tissue_for_research_tier = models.IntegerField(db_column='autopsyTissueForResearchTier', blank=True, null=True)
    prior_malignancy = models.TextField(db_column='priorMalignancy', blank=True, null=True)
    prior_malignancy_tier = models.IntegerField(db_column='priorMalignancyTier', blank=True, null=True)
    date_of_prior_malignancy = models.TextField(db_column='dateOfPriorMalignancy', blank=True, null=True)
    date_of_prior_malignancy_tier = models.IntegerField(db_column='dateOfPriorMalignancyTier', blank=True, null=True)
    family_history_and_risk_factors = models.TextField(db_column='familyHistoryAndRiskFactors', blank=True, null=True)
    family_history_and_risk_factors_tier = models.IntegerField(db_column='familyHistoryAndRiskFactorsTier', blank=True, null=True)
    family_history_of_predisposition_syndrome = models.TextField(db_column='familyHistoryOfPredispositionSyndrome', blank=True, null=True)
    family_history_of_predisposition_syndrome_tier = models.IntegerField(db_column='familyHistoryOfPredispositionSyndromeTier', blank=True, null=True)
    details_of_predisposition_syndrome = models.TextField(db_column='detailsOfPredispositionSyndrome', blank=True, null=True)
    details_of_predisposition_syndrome_tier = models.IntegerField(db_column='detailsOfPredispositionSyndromeTier', blank=True, null=True)
    genetic_cancer_syndrome = models.TextField(db_column='geneticCancerSyndrome', blank=True, null=True)
    genetic_cancer_syndrome_tier = models.IntegerField(db_column='geneticCancerSyndromeTier', blank=True, null=True)
    other_genetic_condition_or_significant_comorbidity = models.TextField(db_column='otherGeneticConditionOrSignificantComorbidity', blank=True, null=True)
    other_genetic_condition_or_significant_comorbidity_tier = models.IntegerField(db_column='otherGeneticConditionOrSignificantComorbidityTier', blank=True, null=True)
    occupational_or_environmental_exposure = models.TextField(db_column='occupationalOrEnvironmentalExposure', blank=True, null=True)
    occupational_or_environmental_exposure_tier = models.IntegerField(db_column='occupationalOrEnvironmentalExposureTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'
        unique_together = (('dataset', 'name'),)


class Radiotherapy(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    course_number = models.TextField(db_column='courseNumber', blank=True, null=True)
    course_number_tier = models.IntegerField(db_column='courseNumberTier', blank=True, null=True)
    start_date = models.TextField(db_column='startDate', blank=True, null=True)
    start_date_tier = models.IntegerField(db_column='startDateTier', blank=True, null=True)
    stop_date = models.TextField(db_column='stopDate', blank=True, null=True)
    stop_date_tier = models.IntegerField(db_column='stopDateTier', blank=True, null=True)
    therapeutic_modality = models.TextField(db_column='therapeuticModality', blank=True, null=True)
    therapeutic_modality_tier = models.IntegerField(db_column='therapeuticModalityTier', blank=True, null=True)
    baseline = models.TextField(blank=True, null=True)
    baseline_tier = models.IntegerField(db_column='baselineTier', blank=True, null=True)
    test_result = models.TextField(db_column='testResult', blank=True, null=True)
    test_result_tier = models.IntegerField(db_column='testResultTier', blank=True, null=True)
    test_result_std = models.TextField(db_column='testResultStd', blank=True, null=True)
    test_result_std_tier = models.IntegerField(db_column='testResultStdTier', blank=True, null=True)
    treating_centre_name = models.TextField(db_column='treatingCentreName', blank=True, null=True)
    treating_centre_name_tier = models.IntegerField(db_column='treatingCentreNameTier', blank=True, null=True)
    start_interval_rad = models.TextField(db_column='startIntervalRad', blank=True, null=True)
    start_interval_rad_tier = models.IntegerField(db_column='startIntervalRadTier', blank=True, null=True)
    start_interval_rad_raw = models.TextField(db_column='startIntervalRadRaw', blank=True, null=True)
    start_interval_rad_raw_tier = models.IntegerField(db_column='startIntervalRadRawTier', blank=True, null=True)
    recording_date = models.TextField(db_column='recordingDate', blank=True, null=True)
    recording_date_tier = models.IntegerField(db_column='recordingDateTier', blank=True, null=True)
    adjacent_fields = models.TextField(db_column='adjacentFields', blank=True, null=True)
    adjacent_fields_tier = models.IntegerField(db_column='adjacentFieldsTier', blank=True, null=True)
    adjacent_fractions = models.TextField(db_column='adjacentFractions', blank=True, null=True)
    adjacent_fractions_tier = models.IntegerField(db_column='adjacentFractionsTier', blank=True, null=True)
    complete = models.TextField(blank=True, null=True)
    complete_tier = models.IntegerField(db_column='completeTier', blank=True, null=True)
    brachytherapy_dose = models.TextField(db_column='brachytherapyDose', blank=True, null=True)
    brachytherapy_dose_tier = models.IntegerField(db_column='brachytherapyDoseTier', blank=True, null=True)
    radiotherapy_dose = models.TextField(db_column='radiotherapyDose', blank=True, null=True)
    radiotherapy_dose_tier = models.IntegerField(db_column='radiotherapyDoseTier', blank=True, null=True)
    site_number = models.TextField(db_column='siteNumber', blank=True, null=True)
    site_number_tier = models.IntegerField(db_column='siteNumberTier', blank=True, null=True)
    technique = models.TextField(blank=True, null=True)
    technique_tier = models.IntegerField(db_column='techniqueTier', blank=True, null=True)
    treated_region = models.TextField(db_column='treatedRegion', blank=True, null=True)
    treated_region_tier = models.IntegerField(db_column='treatedRegionTier', blank=True, null=True)
    treatment_plan_id = models.TextField(db_column='treatmentPlanId', blank=True, null=True)
    treatment_plan_id_tier = models.IntegerField(db_column='treatmentPlanIdTier', blank=True, null=True)
    radiation_type = models.TextField(db_column='radiationType', blank=True, null=True)
    radiation_type_tier = models.IntegerField(db_column='radiationTypeTier', blank=True, null=True)
    radiation_site = models.TextField(db_column='radiationSite', blank=True, null=True)
    radiation_site_tier = models.IntegerField(db_column='radiationSiteTier', blank=True, null=True)
    total_dose = models.TextField(db_column='totalDose', blank=True, null=True)
    total_dose_tier = models.IntegerField(db_column='totalDoseTier', blank=True, null=True)
    boost_site = models.TextField(db_column='boostSite', blank=True, null=True)
    boost_site_tier = models.IntegerField(db_column='boostSiteTier', blank=True, null=True)
    boost_dose = models.TextField(db_column='boostDose', blank=True, null=True)
    boost_dose_tier = models.IntegerField(db_column='boostDoseTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'radiotherapy'
        unique_together = (('dataset', 'name'),)


class Sample(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    #patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING, to_field='patient_id', db_column='patientId')
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    sample_id = models.TextField(db_column='sampleId', blank=True, null=True, unique=True)
    sample_id_tier = models.IntegerField(db_column='sampleIdTier', blank=True, null=True)
    # TODO: not unique?
    diagnosis_id = models.TextField(db_column='diagnosisId', blank=True, null=True)
    #diagnosis_id = models.ForeignKey(Diagnosis, models.DO_NOTHING, to_field='diagnosis_id', db_column='diagnosisId')
    diagnosis_id_tier = models.IntegerField(db_column='diagnosisIdTier', blank=True, null=True)
    local_biobank_id = models.TextField(db_column='localBiobankId', blank=True, null=True)
    local_biobank_id_tier = models.IntegerField(db_column='localBiobankIdTier', blank=True, null=True)
    collection_date = models.TextField(db_column='collectionDate', blank=True, null=True)
    collection_date_tier = models.IntegerField(db_column='collectionDateTier', blank=True, null=True)
    collection_hospital = models.TextField(db_column='collectionHospital', blank=True, null=True)
    collection_hospital_tier = models.IntegerField(db_column='collectionHospitalTier', blank=True, null=True)
    sample_type = models.TextField(db_column='sampleType', blank=True, null=True)
    sample_type_tier = models.IntegerField(db_column='sampleTypeTier', blank=True, null=True)
    tissue_disease_state = models.TextField(db_column='tissueDiseaseState', blank=True, null=True)
    tissue_disease_state_tier = models.IntegerField(db_column='tissueDiseaseStateTier', blank=True, null=True)
    anatomic_site_the_sample_obtained_from = models.TextField(db_column='anatomicSiteTheSampleObtainedFrom', blank=True, null=True)
    anatomic_site_the_sample_obtained_from_tier = models.IntegerField(db_column='anatomicSiteTheSampleObtainedFromTier', blank=True, null=True)
    cancer_type = models.TextField(db_column='cancerType', blank=True, null=True)
    cancer_type_tier = models.IntegerField(db_column='cancerTypeTier', blank=True, null=True)
    cancer_subtype = models.TextField(db_column='cancerSubtype', blank=True, null=True)
    cancer_subtype_tier = models.IntegerField(db_column='cancerSubtypeTier', blank=True, null=True)
    pathology_report_id = models.TextField(db_column='pathologyReportId', blank=True, null=True)
    pathology_report_id_tier = models.IntegerField(db_column='pathologyReportIdTier', blank=True, null=True)
    morphological_code = models.TextField(db_column='morphologicalCode', blank=True, null=True)
    morphological_code_tier = models.IntegerField(db_column='morphologicalCodeTier', blank=True, null=True)
    topological_code = models.TextField(db_column='topologicalCode', blank=True, null=True)
    topological_code_tier = models.IntegerField(db_column='topologicalCodeTier', blank=True, null=True)
    shipping_date = models.TextField(db_column='shippingDate', blank=True, null=True)
    shipping_date_tier = models.IntegerField(db_column='shippingDateTier', blank=True, null=True)
    received_date = models.TextField(db_column='receivedDate', blank=True, null=True)
    received_date_tier = models.IntegerField(db_column='receivedDateTier', blank=True, null=True)
    quality_control_performed = models.TextField(db_column='qualityControlPerformed', blank=True, null=True)
    quality_control_performed_tier = models.IntegerField(db_column='qualityControlPerformedTier', blank=True, null=True)
    estimated_tumor_content = models.TextField(db_column='estimatedTumorContent', blank=True, null=True)
    estimated_tumor_content_tier = models.IntegerField(db_column='estimatedTumorContentTier', blank=True, null=True)
    quantity = models.TextField(blank=True, null=True)
    quantity_tier = models.IntegerField(db_column='quantityTier', blank=True, null=True)
    units = models.TextField(blank=True, null=True)
    units_tier = models.IntegerField(db_column='unitsTier', blank=True, null=True)
    associated_biobank = models.TextField(db_column='associatedBiobank', blank=True, null=True)
    associated_biobank_tier = models.IntegerField(db_column='associatedBiobankTier', blank=True, null=True)
    other_biobank = models.TextField(db_column='otherBiobank', blank=True, null=True)
    other_biobank_tier = models.IntegerField(db_column='otherBiobankTier', blank=True, null=True)
    sop_followed = models.TextField(db_column='sopFollowed', blank=True, null=True)
    sop_followed_tier = models.IntegerField(db_column='sopFollowedTier', blank=True, null=True)
    if_not_explain_any_deviation = models.TextField(db_column='ifNotExplainAnyDeviation', blank=True, null=True)
    if_not_explain_any_deviation_tier = models.IntegerField(db_column='ifNotExplainAnyDeviationTier', blank=True, null=True)
    recording_date = models.TextField(db_column='recordingDate', blank=True, null=True)
    recording_date_tier = models.IntegerField(db_column='recordingDateTier', blank=True, null=True)
    start_interval = models.TextField(db_column='startInterval', blank=True, null=True)
    start_interval_tier = models.IntegerField(db_column='startIntervalTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample'
        unique_together = (('dataset', 'name'),)

    def generate_name(self, patient_id):
        self.name = f"{patient_id}_{self.sample_id}"


class SampleURL(models.Model):
    # TODO: useless normally, but need it because not managed
    id = models.IntegerField(primary_key=True)
    sample_id = models.ForeignKey(Sample, models.DO_NOTHING, to_field='sample_id', db_column='sampleId')
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'sample_url'


class Sequencing(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sequencing_id = models.TextField(db_column='sequencingId', blank=True, null=True)
    sequencing_id_tier = models.IntegerField(db_column='sequencingIdTier', blank=True, null=True)
    #sample_id = models.TextField(db_column='sampleId', blank=True, null=True)
    sample_id = models.ForeignKey(Sample, models.DO_NOTHING, to_field='sample_id', db_column='sampleId')
    sample_id_tier = models.IntegerField(db_column='sampleIdTier', blank=True, null=True)
    dna_library_kit = models.TextField(db_column='dnaLibraryKit', blank=True, null=True)
    dna_library_kit_tier = models.IntegerField(db_column='dnaLibraryKitTier', blank=True, null=True)
    dna_seq_platform = models.TextField(db_column='dnaSeqPlatform', blank=True, null=True)
    dna_seq_platform_tier = models.IntegerField(db_column='dnaSeqPlatformTier', blank=True, null=True)
    dna_read_length = models.TextField(db_column='dnaReadLength', blank=True, null=True)
    dna_read_length_tier = models.IntegerField(db_column='dnaReadLengthTier', blank=True, null=True)
    rna_library_kit = models.TextField(db_column='rnaLibraryKit', blank=True, null=True)
    rna_library_kit_tier = models.IntegerField(db_column='rnaLibraryKitTier', blank=True, null=True)
    rna_seq_platform = models.TextField(db_column='rnaSeqPlatform', blank=True, null=True)
    rna_seq_platform_tier = models.IntegerField(db_column='rnaSeqPlatformTier', blank=True, null=True)
    rna_read_length = models.TextField(db_column='rnaReadLength', blank=True, null=True)
    rna_read_length_tier = models.IntegerField(db_column='rnaReadLengthTier', blank=True, null=True)
    pcr_cycles = models.TextField(db_column='pcrCycles', blank=True, null=True)
    pcr_cycles_tier = models.IntegerField(db_column='pcrCyclesTier', blank=True, null=True)
    extraction_id = models.TextField(db_column='extractionId', blank=True, null=True)
    extraction_id_tier = models.IntegerField(db_column='extractionIdTier', blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    site_tier = models.IntegerField(db_column='siteTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sequencing'
        unique_together = (('dataset', 'name'),)


class Slide(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    sample_id = models.TextField(db_column='sampleId', blank=True, null=True)
    sample_id_tier = models.IntegerField(db_column='sampleIdTier', blank=True, null=True)
    slide_id = models.TextField(db_column='slideId', blank=True, null=True)
    slide_id_tier = models.IntegerField(db_column='slideIdTier', blank=True, null=True)
    slide_other_id = models.TextField(db_column='slideOtherId', blank=True, null=True)
    slide_other_id_tier = models.IntegerField(db_column='slideOtherIdTier', blank=True, null=True)
    lymphocyte_infiltration_percent = models.TextField(db_column='lymphocyteInfiltrationPercent', blank=True, null=True)
    lymphocyte_infiltration_percent_tier = models.IntegerField(db_column='lymphocyteInfiltrationPercentTier', blank=True, null=True)
    tumor_nuclei_percent = models.TextField(db_column='tumorNucleiPercent', blank=True, null=True)
    tumor_nuclei_percent_tier = models.IntegerField(db_column='tumorNucleiPercentTier', blank=True, null=True)
    monocyte_infiltration_percent = models.TextField(db_column='monocyteInfiltrationPercent', blank=True, null=True)
    monocyte_infiltration_percent_tier = models.IntegerField(db_column='monocyteInfiltrationPercentTier', blank=True, null=True)
    normal_cells_percent = models.TextField(db_column='normalCellsPercent', blank=True, null=True)
    normal_cells_percent_tier = models.IntegerField(db_column='normalCellsPercentTier', blank=True, null=True)
    tumor_cells_percent = models.TextField(db_column='tumorCellsPercent', blank=True, null=True)
    tumor_cells_percent_tier = models.IntegerField(db_column='tumorCellsPercentTier', blank=True, null=True)
    stromal_cells_percent = models.TextField(db_column='stromalCellsPercent', blank=True, null=True)
    stromal_cells_percent_tier = models.IntegerField(db_column='stromalCellsPercentTier', blank=True, null=True)
    eosinophil_infiltration_percent = models.TextField(db_column='eosinophilInfiltrationPercent', blank=True, null=True)
    eosinophil_infiltration_percent_tier = models.IntegerField(db_column='eosinophilInfiltrationPercentTier', blank=True, null=True)
    neutrophil_infiltration_percent = models.TextField(db_column='neutrophilInfiltrationPercent', blank=True, null=True)
    neutrophil_infiltration_percent_tier = models.IntegerField(db_column='neutrophilInfiltrationPercentTier', blank=True, null=True)
    granulocyte_infiltration_percent = models.TextField(db_column='granulocyteInfiltrationPercent', blank=True, null=True)
    granulocyte_infiltration_percent_tier = models.IntegerField(db_column='granulocyteInfiltrationPercentTier', blank=True, null=True)
    necrosis_percent = models.TextField(db_column='necrosisPercent', blank=True, null=True)
    necrosis_percent_tier = models.IntegerField(db_column='necrosisPercentTier', blank=True, null=True)
    inflammatory_infiltration_percent = models.TextField(db_column='inflammatoryInfiltrationPercent', blank=True, null=True)
    inflammatory_infiltration_percent_tier = models.IntegerField(db_column='inflammatoryInfiltrationPercentTier', blank=True, null=True)
    proliferating_cells_number = models.TextField(db_column='proliferatingCellsNumber', blank=True, null=True)
    proliferating_cells_number_tier = models.IntegerField(db_column='proliferatingCellsNumberTier', blank=True, null=True)
    section_location = models.TextField(db_column='sectionLocation', blank=True, null=True)
    section_location_tier = models.IntegerField(db_column='sectionLocationTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'slide'
        unique_together = (('dataset', 'name'),)

    def generate_name(self, patient_id):
        self.name = f"{patient_id}_{self.slide_id}"


class Study(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    start_date = models.TextField(db_column='startDate', blank=True, null=True)
    start_date_tier = models.IntegerField(db_column='startDateTier', blank=True, null=True)
    end_date = models.TextField(db_column='endDate', blank=True, null=True)
    end_date_tier = models.IntegerField(db_column='endDateTier', blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    status_tier = models.IntegerField(db_column='statusTier', blank=True, null=True)
    recording_date = models.TextField(db_column='recordingDate', blank=True, null=True)
    recording_date_tier = models.IntegerField(db_column='recordingDateTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'study'
        unique_together = (('dataset', 'name'),)

    def generate_name(self, patient_id):
        self.name = f"{patient_id}_{self.start_date}"


class Surgery(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    start_date = models.TextField(db_column='startDate', blank=True, null=True)
    start_date_tier = models.IntegerField(db_column='startDateTier', blank=True, null=True)
    stop_date = models.TextField(db_column='stopDate', blank=True, null=True)
    stop_date_tier = models.IntegerField(db_column='stopDateTier', blank=True, null=True)
    #sample_id = models.TextField(db_column='sampleId', blank=True, null=True)
    sample_id = models.ForeignKey(Sample, models.DO_NOTHING, to_field='sample_id', db_column='sampleId')
    sample_id_tier = models.IntegerField(db_column='sampleIdTier', blank=True, null=True)
    collection_time_point = models.TextField(db_column='collectionTimePoint', blank=True, null=True)
    collection_time_point_tier = models.IntegerField(db_column='collectionTimePointTier', blank=True, null=True)
    diagnosis_date = models.TextField(db_column='diagnosisDate', blank=True, null=True)
    diagnosis_date_tier = models.IntegerField(db_column='diagnosisDateTier', blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    site_tier = models.IntegerField(db_column='siteTier', blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    type_tier = models.IntegerField(db_column='typeTier', blank=True, null=True)
    recording_date = models.TextField(db_column='recordingDate', blank=True, null=True)
    recording_date_tier = models.IntegerField(db_column='recordingDateTier', blank=True, null=True)
    treatment_plan_id = models.TextField(db_column='treatmentPlanId', blank=True, null=True)
    treatment_plan_id_tier = models.IntegerField(db_column='treatmentPlanIdTier', blank=True, null=True)
    course_number = models.TextField(db_column='courseNumber', blank=True, null=True)
    course_number_tier = models.IntegerField(db_column='courseNumberTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surgery'
        unique_together = (('dataset', 'name'),)


class System(models.Model):
    key = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'system'


class Treatment(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    course_number = models.TextField(db_column='courseNumber', blank=True, null=True)
    course_number_tier = models.IntegerField(db_column='courseNumberTier', blank=True, null=True)
    therapeutic_modality = models.TextField(db_column='therapeuticModality', blank=True, null=True)
    therapeutic_modality_tier = models.IntegerField(db_column='therapeuticModalityTier', blank=True, null=True)
    systematic_therapy_agent_name = models.TextField(db_column='systematicTherapyAgentName', blank=True, null=True)
    systematic_therapy_agent_name_tier = models.IntegerField(db_column='systematicTherapyAgentNameTier', blank=True, null=True)
    treatment_plan_type = models.TextField(db_column='treatmentPlanType', blank=True, null=True)
    treatment_plan_type_tier = models.IntegerField(db_column='treatmentPlanTypeTier', blank=True, null=True)
    treatment_intent = models.TextField(db_column='treatmentIntent', blank=True, null=True)
    treatment_intent_tier = models.IntegerField(db_column='treatmentIntentTier', blank=True, null=True)
    start_date = models.TextField(db_column='startDate', blank=True, null=True)
    start_date_tier = models.IntegerField(db_column='startDateTier', blank=True, null=True)
    stop_date = models.TextField(db_column='stopDate', blank=True, null=True)
    stop_date_tier = models.IntegerField(db_column='stopDateTier', blank=True, null=True)
    reason_for_ending_the_treatment = models.TextField(db_column='reasonForEndingTheTreatment', blank=True, null=True)
    reason_for_ending_the_treatment_tier = models.IntegerField(db_column='reasonForEndingTheTreatmentTier', blank=True, null=True)
    response_to_treatment = models.TextField(db_column='responseToTreatment', blank=True, null=True)
    response_to_treatment_tier = models.IntegerField(db_column='responseToTreatmentTier', blank=True, null=True)
    response_criteria_used = models.TextField(db_column='responseCriteriaUsed', blank=True, null=True)
    response_criteria_used_tier = models.IntegerField(db_column='responseCriteriaUsedTier', blank=True, null=True)
    date_of_recurrence_or_progression_after_this_treatment = models.TextField(db_column='dateOfRecurrenceOrProgressionAfterThisTreatment', blank=True, null=True)
    date_of_recurrence_or_progression_after_this_treatment_tier = models.IntegerField(db_column='dateOfRecurrenceOrProgressionAfterThisTreatmentTier', blank=True, null=True)
    unexpected_or_unusual_toxicity_during_treatment = models.TextField(db_column='unexpectedOrUnusualToxicityDuringTreatment', blank=True, null=True)
    unexpected_or_unusual_toxicity_during_treatment_tier = models.IntegerField(db_column='unexpectedOrUnusualToxicityDuringTreatmentTier', blank=True, null=True)
    drug_id_numbers = models.TextField(db_column='drugIdNumbers', blank=True, null=True)
    drug_id_numbers_tier = models.IntegerField(db_column='drugIdNumbersTier', blank=True, null=True)
    diagnosis_id = models.TextField(db_column='diagnosisId', blank=True, null=True)
    diagnosis_id_tier = models.IntegerField(db_column='diagnosisIdTier', blank=True, null=True)
    treatment_plan_id = models.TextField(db_column='treatmentPlanId', blank=True, null=True)
    treatment_plan_id_tier = models.IntegerField(db_column='treatmentPlanIdTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treatment'
        unique_together = (('dataset', 'name'),)

    def generate_name(self, patient_id):
        self.name = f"{patient_id}_{self.start_date}"

class Tumourboard(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.TextField(db_column='patientId', blank=True, null=True)
    patient_id_tier = models.IntegerField(db_column='patientIdTier', blank=True, null=True)
    date_of_molecular_tumor_board = models.TextField(db_column='dateOfMolecularTumorBoard', blank=True, null=True)
    date_of_molecular_tumor_board_tier = models.IntegerField(db_column='dateOfMolecularTumorBoardTier', blank=True, null=True)
    type_of_sample_analyzed = models.TextField(db_column='typeOfSampleAnalyzed', blank=True, null=True)
    type_of_sample_analyzed_tier = models.IntegerField(db_column='typeOfSampleAnalyzedTier', blank=True, null=True)
    type_of_tumour_sample_analyzed = models.TextField(db_column='typeOfTumourSampleAnalyzed', blank=True, null=True)
    type_of_tumour_sample_analyzed_tier = models.IntegerField(db_column='typeOfTumourSampleAnalyzedTier', blank=True, null=True)
    analyses_discussed = models.TextField(db_column='analysesDiscussed', blank=True, null=True)
    analyses_discussed_tier = models.IntegerField(db_column='analysesDiscussedTier', blank=True, null=True)
    somatic_sample_type = models.TextField(db_column='somaticSampleType', blank=True, null=True)
    somatic_sample_type_tier = models.IntegerField(db_column='somaticSampleTypeTier', blank=True, null=True)
    normal_expression_comparator = models.TextField(db_column='normalExpressionComparator', blank=True, null=True)
    normal_expression_comparator_tier = models.IntegerField(db_column='normalExpressionComparatorTier', blank=True, null=True)
    disease_expression_comparator = models.TextField(db_column='diseaseExpressionComparator', blank=True, null=True)
    disease_expression_comparator_tier = models.IntegerField(db_column='diseaseExpressionComparatorTier', blank=True, null=True)
    has_a_germline_variant_been_identified_by_profiling_that_may_predispose_to_cancer = models.TextField(db_column='hasAGermlineVariantBeenIdentifiedByProfilingThatMayPredisposeToCancer', blank=True, null=True)
    has_a_germline_variant_been_identified_by_profiling_that_may_predispose_to_cancer_tier = models.IntegerField(db_column='hasAGermlineVariantBeenIdentifiedByProfilingThatMayPredisposeToCancerTier', blank=True, null=True)
    actionable_target_found = models.TextField(db_column='actionableTargetFound', blank=True, null=True)
    actionable_target_found_tier = models.IntegerField(db_column='actionableTargetFoundTier', blank=True, null=True)
    molecular_tumor_board_recommendation = models.TextField(db_column='molecularTumorBoardRecommendation', blank=True, null=True)
    molecular_tumor_board_recommendation_tier = models.IntegerField(db_column='molecularTumorBoardRecommendationTier', blank=True, null=True)
    germline_dna_sample_id = models.TextField(db_column='germlineDnaSampleId', blank=True, null=True)
    germline_dna_sample_id_tier = models.IntegerField(db_column='germlineDnaSampleIdTier', blank=True, null=True)
    tumor_dna_sample_id = models.TextField(db_column='tumorDnaSampleId', blank=True, null=True)
    tumor_dna_sample_id_tier = models.IntegerField(db_column='tumorDnaSampleIdTier', blank=True, null=True)
    tumor_rna_sample_id = models.TextField(db_column='tumorRnaSampleId', blank=True, null=True)
    tumor_rna_sample_id_tier = models.IntegerField(db_column='tumorRnaSampleIdTier', blank=True, null=True)
    germline_snv_discussed = models.TextField(db_column='germlineSnvDiscussed', blank=True, null=True)
    germline_snv_discussed_tier = models.IntegerField(db_column='germlineSnvDiscussedTier', blank=True, null=True)
    somatic_snv_discussed = models.TextField(db_column='somaticSnvDiscussed', blank=True, null=True)
    somatic_snv_discussed_tier = models.IntegerField(db_column='somaticSnvDiscussedTier', blank=True, null=True)
    cnvs_discussed = models.TextField(db_column='cnvsDiscussed', blank=True, null=True)
    cnvs_discussed_tier = models.IntegerField(db_column='cnvsDiscussedTier', blank=True, null=True)
    structural_variant_discussed = models.TextField(db_column='structuralVariantDiscussed', blank=True, null=True)
    structural_variant_discussed_tier = models.IntegerField(db_column='structuralVariantDiscussedTier', blank=True, null=True)
    classification_of_variants = models.TextField(db_column='classificationOfVariants', blank=True, null=True)
    classification_of_variants_tier = models.IntegerField(db_column='classificationOfVariantsTier', blank=True, null=True)
    clinical_validation_progress = models.TextField(db_column='clinicalValidationProgress', blank=True, null=True)
    clinical_validation_progress_tier = models.IntegerField(db_column='clinicalValidationProgressTier', blank=True, null=True)
    type_of_validation = models.TextField(db_column='typeOfValidation', blank=True, null=True)
    type_of_validation_tier = models.IntegerField(db_column='typeOfValidationTier', blank=True, null=True)
    agent_or_drug_class = models.TextField(db_column='agentOrDrugClass', blank=True, null=True)
    agent_or_drug_class_tier = models.IntegerField(db_column='agentOrDrugClassTier', blank=True, null=True)
    level_of_evidence_for_expression_target_agent_match = models.TextField(db_column='levelOfEvidenceForExpressionTargetAgentMatch', blank=True, null=True)
    level_of_evidence_for_expression_target_agent_match_tier = models.IntegerField(db_column='levelOfEvidenceForExpressionTargetAgentMatchTier', blank=True, null=True)
    did_treatment_plan_change_based_on_profiling_result = models.TextField(db_column='didTreatmentPlanChangeBasedOnProfilingResult', blank=True, null=True)
    did_treatment_plan_change_based_on_profiling_result_tier = models.IntegerField(db_column='didTreatmentPlanChangeBasedOnProfilingResultTier', blank=True, null=True)
    how_treatment_has_altered_based_on_profiling = models.TextField(db_column='howTreatmentHasAlteredBasedOnProfiling', blank=True, null=True)
    how_treatment_has_altered_based_on_profiling_tier = models.IntegerField(db_column='howTreatmentHasAlteredBasedOnProfilingTier', blank=True, null=True)
    reason_treatment_plan_did_not_change_based_on_profiling = models.TextField(db_column='reasonTreatmentPlanDidNotChangeBasedOnProfiling', blank=True, null=True)
    reason_treatment_plan_did_not_change_based_on_profiling_tier = models.IntegerField(db_column='reasonTreatmentPlanDidNotChangeBasedOnProfilingTier', blank=True, null=True)
    details_of_treatment_plan_impact = models.TextField(db_column='detailsOfTreatmentPlanImpact', blank=True, null=True)
    details_of_treatment_plan_impact_tier = models.IntegerField(db_column='detailsOfTreatmentPlanImpactTier', blank=True, null=True)
    patient_or_family_informed_of_germline_variant = models.TextField(db_column='patientOrFamilyInformedOfGermlineVariant', blank=True, null=True)
    patient_or_family_informed_of_germline_variant_tier = models.IntegerField(db_column='patientOrFamilyInformedOfGermlineVariantTier', blank=True, null=True)
    patient_has_been_referred_to_a_hereditary_cancer_program_based_on_this_molecular_profiling = models.TextField(db_column='patientHasBeenReferredToAHereditaryCancerProgramBasedOnThisMolecularProfiling', blank=True, null=True)
    patient_has_been_referred_to_a_hereditary_cancer_program_based_on_this_molecular_profiling_tier = models.IntegerField(db_column='patientHasBeenReferredToAHereditaryCancerProgramBasedOnThisMolecularProfilingTier', blank=True, null=True)
    summary_report = models.TextField(db_column='summaryReport', blank=True, null=True)
    summary_report_tier = models.IntegerField(db_column='summaryReportTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tumourboard'
        unique_together = (('dataset', 'name'),)

    def generate_name(self, patient_id):
        self.name = f"{patient_id}_{self.date_of_molecular_tumor_board}"


class Variantcalling(models.Model):
    id = models.TextField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    dataset = models.ForeignKey(Dataset, models.DO_NOTHING, db_column='datasetId')
    created = models.TextField()
    updated = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    variant_calling_id = models.TextField(db_column='variantCallingId', blank=True, null=True)
    variant_calling_id_tier = models.IntegerField(db_column='variantCallingIdTier', blank=True, null=True)
    sample_id = models.TextField(db_column='sampleId', blank=True, null=True)
    sample_id_tier = models.IntegerField(db_column='sampleIdTier', blank=True, null=True)
    in_house_pipeline = models.TextField(db_column='inHousePipeline', blank=True, null=True)
    in_house_pipeline_tier = models.IntegerField(db_column='inHousePipelineTier', blank=True, null=True)
    variant_caller = models.TextField(db_column='variantCaller', blank=True, null=True)
    variant_caller_tier = models.IntegerField(db_column='variantCallerTier', blank=True, null=True)
    tabulate = models.TextField(blank=True, null=True)
    tabulate_tier = models.IntegerField(db_column='tabulateTier', blank=True, null=True)
    annotation = models.TextField(blank=True, null=True)
    annotation_tier = models.IntegerField(db_column='annotationTier', blank=True, null=True)
    merge_tool = models.TextField(db_column='mergeTool', blank=True, null=True)
    merge_tool_tier = models.IntegerField(db_column='mergeToolTier', blank=True, null=True)
    rda_to_tab = models.TextField(db_column='rdaToTab', blank=True, null=True)
    rda_to_tab_tier = models.IntegerField(db_column='rdaToTabTier', blank=True, null=True)
    delly = models.TextField(blank=True, null=True)
    delly_tier = models.IntegerField(db_column='dellyTier', blank=True, null=True)
    post_filter = models.TextField(db_column='postFilter', blank=True, null=True)
    post_filter_tier = models.IntegerField(db_column='postFilterTier', blank=True, null=True)
    clip_filter = models.TextField(db_column='clipFilter', blank=True, null=True)
    clip_filter_tier = models.IntegerField(db_column='clipFilterTier', blank=True, null=True)
    cosmic = models.TextField(blank=True, null=True)
    cosmic_tier = models.IntegerField(db_column='cosmicTier', blank=True, null=True)
    db_snp = models.TextField(db_column='dbSnp', blank=True, null=True)
    db_snp_tier = models.IntegerField(db_column='dbSnpTier', blank=True, null=True)
    alignment_id = models.TextField(db_column='alignmentId', blank=True, null=True)
    alignment_id_tier = models.IntegerField(db_column='alignmentIdTier', blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    site_tier = models.IntegerField(db_column='siteTier', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variantcalling'
        unique_together = (('dataset', 'name'),)
