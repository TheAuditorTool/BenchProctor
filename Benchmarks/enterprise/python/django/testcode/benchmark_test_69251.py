# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69251(request):
    host_value = request.META.get('HTTP_HOST', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(host_value)})
