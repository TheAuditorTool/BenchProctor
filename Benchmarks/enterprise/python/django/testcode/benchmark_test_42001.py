# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42001(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
