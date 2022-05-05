from rest_framework import serializers
from itc_backend.apps.core.models import Executive, ExecutiveYear


class ExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executive
        fields = "__all__"


class ExecutiveYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutiveYear
        fields = "__all__"

