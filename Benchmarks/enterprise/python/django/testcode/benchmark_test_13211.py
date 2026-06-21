# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest13211(request):
    upload_name = request.FILES['upload'].name
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(upload_name)))
    return JsonResponse({"saved": True})
