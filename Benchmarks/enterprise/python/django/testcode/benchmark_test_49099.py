# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest49099(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return JsonResponse({"saved": True})
