# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest57946(request):
    env_value = os.environ.get('USER_INPUT', '')
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(env_value).encode())
    return JsonResponse({"saved": True})
