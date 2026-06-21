# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
from urllib.parse import unquote


def BenchmarkTest74064(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
