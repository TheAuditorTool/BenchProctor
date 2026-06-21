# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02815(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    eval(str(data))
    return JsonResponse({"saved": True})
