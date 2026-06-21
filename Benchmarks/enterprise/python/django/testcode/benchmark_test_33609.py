# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest33609(request):
    user_id = request.GET.get('id', '')
    data = ensure_str(user_id)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JsonResponse({'record': str(record)}, status=200)
