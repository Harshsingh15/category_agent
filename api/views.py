from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from services.categorization_agent import CategorizationAgent


agent = CategorizationAgent()


@api_view(['POST'])
def categorize_transaction(request):

    data = request.data

    transaction = data.get("transaction")
    company_context = data.get("company_context")

    result = agent.categorize(transaction, company_context)

    return Response(result)