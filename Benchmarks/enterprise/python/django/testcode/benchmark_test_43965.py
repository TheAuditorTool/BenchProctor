# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest43965(request):
    secret_value = 'app_display_name'
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
