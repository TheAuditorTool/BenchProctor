# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06471(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
