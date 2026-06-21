# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest66596(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % (cookie_value,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
