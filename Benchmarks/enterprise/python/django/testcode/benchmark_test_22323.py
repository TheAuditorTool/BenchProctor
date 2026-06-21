# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest22323(request):
    user_id = request.GET.get('id', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(user_id),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
