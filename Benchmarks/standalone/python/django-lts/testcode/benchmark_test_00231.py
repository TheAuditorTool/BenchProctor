# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from Crypto.Hash import SHA256
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00231(request, path_param):
    path_value = path_param
    form = FormData(payload=path_value)
    data = form.payload
    digest = SHA256.new(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
