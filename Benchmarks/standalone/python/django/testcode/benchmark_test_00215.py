# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00215(request):
    field_value = request.POST.get('field', '')
    parts = str(field_value).split(',')
    data = ' '.join(parts)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
