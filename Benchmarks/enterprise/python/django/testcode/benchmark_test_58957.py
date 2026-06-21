# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
from urllib.parse import unquote
import os


def BenchmarkTest58957(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return JsonResponse({'length': len(ciphertext)}, status=200)
