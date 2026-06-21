# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest71545(request):
    xml_value = request.body.decode('utf-8')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(xml_value).encode())
    return JsonResponse({"saved": True})
