# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13367(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(forwarded_ip)})
