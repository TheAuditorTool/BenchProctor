# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest00202(request):
    field_value = request.POST.get('field', '')
    data = '{}'.format(field_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
