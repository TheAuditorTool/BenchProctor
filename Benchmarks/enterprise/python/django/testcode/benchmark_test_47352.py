# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47352(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
