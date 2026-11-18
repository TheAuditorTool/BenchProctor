# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00482(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    form = FormData(payload=referer_value)
    data = form.payload
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
