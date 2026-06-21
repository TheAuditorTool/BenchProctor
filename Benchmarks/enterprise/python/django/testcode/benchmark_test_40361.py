# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40361(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
