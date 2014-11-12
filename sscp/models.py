# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class TDicomPrinter(models.Model):
    dicom_printer_ref = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64L, unique=True)
    ae_title = models.CharField(max_length=32L, unique=True)
    host = models.CharField(max_length=32L)
    port = models.IntegerField()
    max_pdu = models.IntegerField()
    description = models.CharField(max_length=256L, blank=True)
    class Meta:
        db_table = 't_dicom_printer'

class TDicomWorkstation(models.Model):
    dicom_workstation_ref = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64L, unique=True)
    ae_title = models.CharField(max_length=32L, unique=True)
    host = models.CharField(max_length=32L)
    description = models.CharField(max_length=256L, blank=True)
    is_default = models.CharField(max_length=1L)
    dicom_settings = models.TextField()
    class Meta:
        db_table = 't_dicom_workstation'

class TFilm(models.Model):
    film_ref = models.IntegerField(primary_key=True)
    date_time_created = models.DateTimeField()
    film_session_ref = models.ForeignKey('TFilmSession', db_column='film_session_ref')
    film_dataset = models.TextField(blank=True)
    volume_ref = models.ForeignKey('TVolume', db_column='volume_ref')
    film_path = models.CharField(max_length=256L)
    study_uid = models.CharField(max_length=64L)
    series_uid = models.CharField(max_length=64L)
    instance_uid = models.CharField(max_length=64L)
    verify_flag = models.TextField() # This field type is a guess.
    date_time_verified = models.DateTimeField(null=True, blank=True)
    store_flag = models.TextField() # This field type is a guess.
    date_time_stored = models.DateTimeField(null=True, blank=True)
    delete_flag = models.TextField() # This field type is a guess.
    date_time_deleted = models.DateTimeField(null=True, blank=True)
    patient_id = models.CharField(max_length=64L, blank=True)
    patient_name = models.CharField(max_length=255L, blank=True)
    accession_number = models.CharField(max_length=32L, blank=True)
    modality = models.CharField(max_length=32L, blank=True)
    study_date = models.CharField(max_length=10L, blank=True)
    study_time = models.CharField(max_length=16L, blank=True)
    class Meta:
        db_table = 't_film'

class TFilmSession(models.Model):
    film_session_ref = models.IntegerField(primary_key=True)
    date_time_created = models.DateTimeField()
    film_session_uid = models.CharField(max_length=64L, unique=True)
    film_session_dataset = models.TextField()
    src_ae_title = models.CharField(max_length=32L)
    close_flag = models.CharField(max_length=1L)
    date_time_closed = models.DateTimeField(null=True, blank=True)
    verify_flag = models.CharField(max_length=1L)
    date_time_verified = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 't_film_session'

class TJob(models.Model):
    job_ref = models.IntegerField(primary_key=True)
    date_time_created = models.DateTimeField()
    date_time_modified = models.DateTimeField()
    host = models.CharField(max_length=64L)
    film_ref = models.ForeignKey(TFilm, unique=True, db_column='film_ref')
    status = models.CharField(max_length=32L)
    class Meta:
        db_table = 't_job'

class TKiosk(models.Model):
    kiosk_ref = models.IntegerField(primary_key=True)
    host = models.CharField(max_length=64L, unique=True)
    name = models.CharField(max_length=32L, unique=True)
    description = models.CharField(max_length=256L, blank=True)
    film_printer_status = models.CharField(max_length=32L)
    report_printer_status = models.CharField(max_length=32L)
    last_update_time = models.DateTimeField()
    class Meta:
        db_table = 't_kiosk'

class TKioskFilmPaperInfo(models.Model):
    kiosk_film_paper_info_ref = models.IntegerField(primary_key=True)
    kiosk_ref = models.ForeignKey(TKiosk, db_column='kiosk_ref')
    film_paper_type_ref = models.ForeignKey('TSysFilmPaperType', db_column='film_paper_type_ref')
    amount = models.IntegerField()
    class Meta:
        db_table = 't_kiosk_film_paper_info'

class TKioskParam(models.Model):
    kiosk_param_ref = models.IntegerField(primary_key=True)
    kiosk_ref = models.ForeignKey(TKiosk, db_column='kiosk_ref')
    film_threshold = models.IntegerField()
    paper_threshold = models.IntegerField()
    class Meta:
        db_table = 't_kiosk_param'

class TOcrSetting(models.Model):
    ocr_setting_ref = models.IntegerField(primary_key=True)
    ae_title = models.CharField(max_length=32L, unique=True)
    description = models.CharField(max_length=256L, blank=True)
    is_default = models.CharField(max_length=1L)
    rule = models.TextField()
    class Meta:
        db_table = 't_ocr_setting'

class TPatientFilmPrint(models.Model):
    patient_film_print_ref = models.IntegerField(primary_key=True)
    accession_number = models.CharField(max_length=32L)
    film_session_ref = models.ForeignKey(TFilmSession, db_column='film_session_ref')
    last_print_date_time = models.DateTimeField(null=True, blank=True)
    print_count = models.IntegerField()
    class Meta:
        db_table = 't_patient_film_print'

class TPatientReport(models.Model):
    patient_report_ref = models.IntegerField(primary_key=True)
    accession_number = models.CharField(max_length=32L, unique=True)
    report_status = models.CharField(max_length=16L, blank=True)
    report_completed_time = models.DateTimeField(null=True, blank=True)
    patient_id = models.CharField(max_length=64L, blank=True)
    patient_name = models.CharField(max_length=256L, blank=True)
    patient_name_cn = models.CharField(max_length=256L, blank=True)
    class Meta:
        db_table = 't_patient_report'

class TPatientReportPrint(models.Model):
    patient_report_print_ref = models.IntegerField(primary_key=True)
    accession_number = models.CharField(max_length=32L, unique=True)
    print_count = models.IntegerField()
    last_print_date_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 't_patient_report_print'

class TPrintJob(models.Model):
    print_job_ref = models.IntegerField(primary_key=True)
    date_time_created = models.DateTimeField()
    date_time_modified = models.DateTimeField(null=True, blank=True)
    job_created_host = models.CharField(max_length=64L)
    job_creator = models.CharField(max_length=32L)
    host = models.CharField(max_length=64L)
    film_ref_list = models.TextField()
    dicom_printer_ae_title = models.CharField(max_length=32L)
    status = models.CharField(max_length=32L)
    status_info = models.TextField(blank=True)
    class Meta:
        db_table = 't_print_job'

class TRisJob(models.Model):
    ris_job_ref = models.IntegerField(primary_key=True)
    date_time_created = models.DateTimeField()
    date_time_modified = models.DateTimeField(null=True, blank=True)
    job_created_host = models.CharField(max_length=64L)
    type = models.CharField(max_length=16L)
    host = models.CharField(max_length=64L)
    accession_number = models.CharField(max_length=32L)
    film_session_ref = models.IntegerField(null=True, blank=True)
    date_time_printed = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=32L)
    retry_count = models.IntegerField()
    date_time_next_retry = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 't_ris_job'

class TRisJobHistory(models.Model):
    ris_job_ref = models.IntegerField(primary_key=True)
    date_time_created = models.DateTimeField()
    date_time_modified = models.DateTimeField(null=True, blank=True)
    job_created_host = models.CharField(max_length=64L)
    type = models.CharField(max_length=16L)
    host = models.CharField(max_length=64L)
    accession_number = models.CharField(max_length=32L)
    film_session_ref = models.IntegerField(null=True, blank=True)
    date_time_printed = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=32L)
    retry_count = models.IntegerField()
    date_time_next_retry = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 't_ris_job_history'

class TServer(models.Model):
    server_ref = models.IntegerField(primary_key=True)
    host = models.CharField(max_length=64L, unique=True)
    description = models.CharField(max_length=256L, blank=True)
    class Meta:
        db_table = 't_server'

class TService(models.Model):
    service_ref = models.IntegerField(primary_key=True)
    server_ref = models.ForeignKey(TServer, db_column='server_ref')
    service_name = models.CharField(max_length=45L)
    class Meta:
        db_table = 't_service'

class TSysFilmPaperType(models.Model):
    film_paper_type_ref = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=32L, unique=True)
    class Meta:
        db_table = 't_sys_film_paper_type'

class TSysIni(models.Model):
    ini_section = models.CharField(max_length=64L)
    ini_key = models.CharField(max_length=64L)
    ini_value = models.CharField(max_length=64L, blank=True)
    class Meta:
        db_table = 't_sys_ini'

class TSysPrintTimeConfig(models.Model):
    sys_print_time_config_ref = models.IntegerField(primary_key=True)
    printer_type = models.CharField(max_length=32L)
    config_item = models.CharField(max_length=32L)
    station_ae_title = models.CharField(max_length=32L)
    first_print_time = models.IntegerField()
    next_print_time = models.IntegerField()
    class Meta:
        db_table = 't_sys_print_time_config'

class TSysVersion(models.Model):
    module_name = models.CharField(max_length=32L, primary_key=True)
    version = models.CharField(max_length=32L)
    install_date = models.DateTimeField()
    class Meta:
        db_table = 't_sys_version'

class TUser(models.Model):
    user_ref = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=64L)
    login_name = models.CharField(max_length=32L, unique=True)
    role_level = models.IntegerField()
    password = models.CharField(max_length=512L)
    description = models.CharField(max_length=256L, blank=True)
    class Meta:
        db_table = 't_user'

class TVolume(models.Model):
    volume_ref = models.IntegerField(primary_key=True)
    server_ref = models.ForeignKey(TServer, db_column='server_ref')
    volume_name = models.CharField(max_length=45L, blank=True)
    path = models.CharField(max_length=256L, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 't_volume'

class TVpReport(models.Model):
    vp_report_ref = models.IntegerField(primary_key=True)
    date_time_created = models.DateTimeField()
    host = models.CharField(max_length=64L)
    volume_ref = models.ForeignKey(TVolume, db_column='volume_ref')
    report_path = models.CharField(max_length=256L)
    status = models.CharField(max_length=32L)
    date_time_recognized = models.DateTimeField(null=True, blank=True)
    accession_number = models.CharField(max_length=32L, blank=True)
    patient_id = models.CharField(max_length=64L, blank=True)
    class Meta:
        db_table = 't_vp_report'

