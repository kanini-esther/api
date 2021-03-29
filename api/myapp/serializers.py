from rest_framework import serializers
from rest_framework import employees

class employeesSerializers(Serializers.ModelSerializer):
    # creating a class meta for configuration
    class Meta:
        Model=employees
        # fields=('firstname','lastname')
        field=__all__
