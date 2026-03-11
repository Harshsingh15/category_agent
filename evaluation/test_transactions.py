import requests

url = "http://127.0.0.1:8000/categorize/"

tests = [
    {
        "description": "Uber ride to airport",
        "expected": "Travel"
    },
    {
        "description": "Adobe monthly subscription",
        "expected": "Software Subscriptions"
    },
    {
        "description": "Lunch with client",
        "expected": "Meals & Entertainment"
    }
]


for t in tests:

    payload = {
        "transaction": {
            "description": t["description"]
        },
        "company_context": {
            "industry": "Software",
            "chart_of_accounts": [
                "Office Supplies",
                "Travel",
                "Software Subscriptions",
                "Meals & Entertainment"
            ]
        }
    }

    r = requests.post(url, json=payload)

    print(t["description"], r.json())