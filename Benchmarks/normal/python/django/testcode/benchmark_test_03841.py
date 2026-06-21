# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import db


def BenchmarkTest03841(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JsonResponse({'record': str(record)}, status=200)
