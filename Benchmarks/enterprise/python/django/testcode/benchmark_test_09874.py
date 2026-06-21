# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09874(request):
    host_value = request.META.get('HTTP_HOST', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(host_value)})
