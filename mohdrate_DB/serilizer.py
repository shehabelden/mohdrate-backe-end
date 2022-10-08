from rest_framework import serializers
from auth_app.models import *
from mohdrate_DB.models import *
class seen_ser_rel(serializers.ModelSerializer):
    class Meta:
        model = seen_db
        fields = ["time_zone", "seen"]
class session_ser(serializers.ModelSerializer):
    class Meta:
        model = session_db
        fields=["session_name",]
class scientific_material_ser(serializers.ModelSerializer):
    class Meta:
        model = scientific_material_db
        fields = ["scientific_material_name","Image"]
class one_scientific_material_ser(serializers.ModelSerializer):
    session = session_ser(many=True)
    class Meta:
        model = scientific_material_db
        look_up = 'scientific_material_name'
        fields = ["scientific_material_name",'session']
class one_session_ser(serializers.ModelSerializer):
    class Meta:
        model = session_db
        look_up = 'session_name'
        fields=["session_name","session"]
class ansers_ser(serializers.ModelSerializer):
    class Meta:
        model = ansers
        fields="__all__"
class a5tbar_ser(serializers.ModelSerializer):
    anserrelated=ansers_ser(many=True)
    class Meta:
        model = akhtbar
        fields="__all__"
class one_akhtbar_material_ser(serializers.ModelSerializer):
    akhtbar = a5tbar_ser(many=True)
    class Meta:
        model = session_db
        look_up = 'session_name'
        fields = ["session_name",'akhtbar']
