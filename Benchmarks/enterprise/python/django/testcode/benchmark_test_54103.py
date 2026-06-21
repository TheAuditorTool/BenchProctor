# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest54103(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(header_value).encode())
    return JsonResponse({"saved": True})
