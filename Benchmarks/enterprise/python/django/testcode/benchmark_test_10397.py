# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10397(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
