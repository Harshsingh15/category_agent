from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from services.categorization_agent import CategorizationAgent
from .serializers import CategorizationRequestSerializer


@api_view(['POST'])
def categorize_transaction(request):

    serializer = CategorizationRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data

    transaction = data.get("transaction")
    company_context = data.get("company_context")

    agent = CategorizationAgent()

    result = agent.categorize(transaction, company_context)

    return Response(result)

@api_view(['GET'])
def health(request):
    return Response({
        "status": "ok",
        "service": "transaction-categorization-agent"
    })