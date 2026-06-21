# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20937(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
