from rest_framework import serializers
from student.models import Students
class StudentSerializers(serializers.ModelSerializer):
    class meta:
        model = Students
        fields = "__all__"