from rest_framework import serializers

from .models import TFilm


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = TFilm
        fields = ('film_ref', 'date_time_created', 'study_uid', 'instance_uid', 'patient_id', 'patient_name',
                  'accession_number')
