from intasend import APIService
publishable_key = "ISPubKey_test_8c36241c-8187-417a-931a-d40a5959b620"
token ="ISSecretKey_test_5b7f5039-31ef-4b4f-ace2-3aa249e2b345"
service = APIService(publishable_key=publishable_key,token=token,test=True)

transactions = [{'name': 'Awesome Customer 1', 'account': 254111383064, 'amount': 1}
                ]

response = service.transfer.mpesa(currency='KES', transactions=transactions)
print(response)
approved_response = service.transfer.approve(response)
print(approved_response)