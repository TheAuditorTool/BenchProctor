# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from dataclasses import dataclass
from django.shortcuts import redirect
import urllib.parse


@dataclass
class FormData:
    payload: str

def BenchmarkTest30968(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
