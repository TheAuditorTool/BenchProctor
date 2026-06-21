# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest60294(request):
    user_id = request.GET.get('id', '')
    data = normalise_input(user_id)
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JsonResponse({'record': str(record)}, status=200)
