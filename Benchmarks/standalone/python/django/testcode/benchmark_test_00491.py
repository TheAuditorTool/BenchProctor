# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00491(request):
    field_value = request.POST.get('field', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(field_value),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
