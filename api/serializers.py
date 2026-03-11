from rest_framework import serializers


class TransactionSerializer(serializers.Serializer):
    description = serializers.CharField(required=True)
    vendor = serializers.CharField(required=False, allow_blank=True)


class CompanyContextSerializer(serializers.Serializer):
    industry = serializers.CharField(required=True)
    chart_of_accounts = serializers.ListField(
        child=serializers.CharField(),
        required=True
    )


class CategorizationRequestSerializer(serializers.Serializer):
    transaction = TransactionSerializer()
    company_context = CompanyContextSerializer()