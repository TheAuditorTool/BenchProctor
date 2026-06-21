# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78809(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
