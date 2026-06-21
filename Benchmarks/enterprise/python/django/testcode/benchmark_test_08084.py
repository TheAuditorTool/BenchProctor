# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest08084(request, path_param):
    path_value = path_param
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(path_value).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
