# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65281(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
