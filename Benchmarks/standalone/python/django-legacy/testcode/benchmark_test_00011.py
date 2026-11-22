# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ctypes
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00011(request):
    field_value = request.POST.get('field', '')
    form = FormData(payload=field_value)
    data = form.payload
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _bounded
    count = int(processed)
    records = ctypes.create_string_buffer(min(count, 65536) * 64)
    return JsonResponse({'allocated': len(records)}, status=200)
