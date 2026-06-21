# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46882(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % (auth_header,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
