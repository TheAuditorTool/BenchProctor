# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15418(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % str(auth_header)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
