# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56908(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
