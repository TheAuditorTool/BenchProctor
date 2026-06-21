# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest62354(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = '%s' % str(dotenv_value)
    Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
