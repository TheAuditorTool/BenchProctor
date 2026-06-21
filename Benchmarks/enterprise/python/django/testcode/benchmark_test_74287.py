# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74287(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
