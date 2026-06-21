# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18329(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
