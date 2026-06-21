# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest53047(request):
    upload_name = request.FILES['upload'].name
    db.execute('SELECT * FROM users WHERE id = ' + str(upload_name))
    return JsonResponse({"saved": True})
