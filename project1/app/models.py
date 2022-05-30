from django.db import models
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class AiAnalysisLog(models.Model):
    image_path = models.CharField(max_length=255, blank=True, null=True)
    success = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.IntegerField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    confidence = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    request_timestamp = models.PositiveIntegerField(blank=True, null=True)
    response_timestamp = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ai_analysis_log'


