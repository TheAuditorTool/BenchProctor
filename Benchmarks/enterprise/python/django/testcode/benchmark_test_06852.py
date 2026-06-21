# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest06852(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
