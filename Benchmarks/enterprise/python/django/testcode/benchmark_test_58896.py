# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest58896(request):
    secret_value = 'app_display_name'
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(secret_value).encode())
    return JsonResponse({"saved": True})
