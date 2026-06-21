# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55310(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
