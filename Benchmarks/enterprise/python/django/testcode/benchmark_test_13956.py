# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13956(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
