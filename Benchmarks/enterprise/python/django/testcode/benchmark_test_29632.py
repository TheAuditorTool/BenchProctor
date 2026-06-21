# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29632(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    prefix = ''
    data = prefix + str(auth_header)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
