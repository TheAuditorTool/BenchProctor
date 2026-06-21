# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest12334(request):
    multipart_value = request.POST.get('multipart_field', '')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(multipart_value).encode())
    return JsonResponse({"saved": True})
