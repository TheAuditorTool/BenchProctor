# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest77561(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
