# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import json


def BenchmarkTest42503(request):
    multipart_value = request.POST.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
