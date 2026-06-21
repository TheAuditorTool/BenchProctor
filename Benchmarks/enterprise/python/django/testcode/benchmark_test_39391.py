# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from dataclasses import dataclass
from django.shortcuts import redirect
import urllib.parse
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest39391(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
