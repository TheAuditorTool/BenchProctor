# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66200(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
