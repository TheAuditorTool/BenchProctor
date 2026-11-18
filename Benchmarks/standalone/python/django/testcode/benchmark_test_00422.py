# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00422(request):
    multipart_value = request.POST.get('multipart_field', '')
    form = FormData(payload=multipart_value)
    data = form.payload
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
