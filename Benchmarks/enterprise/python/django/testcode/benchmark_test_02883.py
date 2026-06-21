# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02883(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
