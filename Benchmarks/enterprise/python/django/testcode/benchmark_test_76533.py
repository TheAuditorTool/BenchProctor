# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76533(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    int(str(data))
    return JsonResponse({"saved": True})
