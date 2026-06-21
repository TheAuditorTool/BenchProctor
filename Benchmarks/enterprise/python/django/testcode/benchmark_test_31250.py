# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import re
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest31250(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
