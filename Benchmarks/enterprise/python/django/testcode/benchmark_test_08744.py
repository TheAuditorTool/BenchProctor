# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08744(request):
    multipart_value = request.POST.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
