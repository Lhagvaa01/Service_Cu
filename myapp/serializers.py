from rest_framework import serializers
from .models import Users, InfoCUBranch, InfoProduct, History


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class InfoCUBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoCUBranch
        fields = '__all__'


class InfoProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoProduct
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    infoProducts = InfoProductSerializer(many=True, read_only=True)

    class Meta:
        model = History
        fields = '__all__'
