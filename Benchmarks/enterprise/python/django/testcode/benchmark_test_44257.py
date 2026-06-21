# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest44257(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    os.remove(str(data))
    return JsonResponse({"saved": True})
