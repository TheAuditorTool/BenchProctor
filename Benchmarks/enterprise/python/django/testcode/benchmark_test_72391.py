# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72391(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
