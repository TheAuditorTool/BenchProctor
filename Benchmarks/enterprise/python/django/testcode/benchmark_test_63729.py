# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest63729(request):
    user_id = request.GET.get('id', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(user_id),))
    if result is None:
        return JsonResponse({'error': 'not found'}, status=404)
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
