# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest66196(request):
    upload_name = request.FILES['upload'].name
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(upload_name),))
    return JsonResponse({"saved": True})
