class PromptBuilder:

    def build(self, transaction, company_context):

        industry = company_context.get("industry")

        chart_of_accounts = company_context.get("chart_of_accounts", [])

        historical = company_context.get("historical_transactions", [])

        categories = "\n".join(chart_of_accounts)

        examples = """
Examples:

Uber ride to airport -> Travel
Flight ticket to London -> Travel
Adobe Creative Cloud subscription -> Software Subscriptions
Lunch with client -> Meals & Entertainment
Bought printer ink -> Office Supplies
"""

        prompt = f"""
You are an accounting assistant responsible for categorizing business expenses.

Industry: {industry}

Valid categories (choose ONLY from these):
{categories}

{examples}

New transaction:
Description: {transaction.get('description')}
Vendor: {transaction.get('vendor','')}

Analyze the transaction and choose the most appropriate category.

Return ONLY valid JSON.

Format:
{{
"category": "",
"confidence": 0-1,
"reasoning": ""
}}

Rules:
- category must be one of the valid categories
- confidence must be between 0 and 1
- do not output anything except JSON
"""

        return prompt