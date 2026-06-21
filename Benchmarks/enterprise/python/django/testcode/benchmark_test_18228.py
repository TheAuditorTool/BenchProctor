# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest18228(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
