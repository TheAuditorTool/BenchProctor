# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest04969(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    ns = SimpleNamespace(payload=profile_value)
    data = getattr(ns, 'payload')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('/var/app/data/' + str(processed), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
