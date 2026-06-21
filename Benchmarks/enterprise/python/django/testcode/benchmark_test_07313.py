# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest07313(request):
    upload_name = request.FILES['upload'].name
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(upload_name),))
    value = result['name']
    return JsonResponse({'name': str(value)}, status=200)
