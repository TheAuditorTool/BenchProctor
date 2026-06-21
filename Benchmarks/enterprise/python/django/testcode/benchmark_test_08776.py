# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08776(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
