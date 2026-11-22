# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest00207(request):
    host_value = request.META.get('HTTP_HOST', '')
    match = re.match(r'^[^@]+@([^@]+)$', str(host_value))
    domain = match.group(1)
    return JsonResponse({'domain': domain}, status=200)
