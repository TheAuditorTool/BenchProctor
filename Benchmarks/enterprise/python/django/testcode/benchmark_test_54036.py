# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54036(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % str(auth_header)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
