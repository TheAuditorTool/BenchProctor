# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03130(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
