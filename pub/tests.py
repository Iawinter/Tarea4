from django.test import TestCase

# Create your tests here.
lista = {
"message": {
"attributes": {
"key": "value"
},
"data": "SGVsbG8gQ2xvdWQgUHViL1N1YiEgSGVyZSBpcyBteSBtZXNzYWdlIQ==",
"messageId": "2070443601311540",
"message_id": "2070443601311540",
"publishTime": "2021-02-26T19:13:55.749Z",
"publish_time": "2021-02-26T19:13:55.749Z",
},
"subscription": "projects/taller-integracion-310700/subscriptions/user_{ID_ALUMNO}"
}

print(lista['message']['data'])