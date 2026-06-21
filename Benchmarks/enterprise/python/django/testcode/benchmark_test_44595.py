# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest44595(request):
    upload_name = request.FILES['upload'].name
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(upload_name),))
    return JsonResponse({'record': str(record)}, status=200)
