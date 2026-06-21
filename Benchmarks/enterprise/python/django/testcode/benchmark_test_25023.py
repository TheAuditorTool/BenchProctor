# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest25023(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = FormData(payload=host_value).payload
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JsonResponse({'record': str(record)}, status=200)
