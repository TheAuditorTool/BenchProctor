# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import re
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest78129(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ensure_str(db_value)
    if not re.fullmatch('^[\\w\\s<>\\"\'/().;=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
