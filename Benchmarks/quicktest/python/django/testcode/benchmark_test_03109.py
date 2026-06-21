# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03109(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
