# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11561(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
