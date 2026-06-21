# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33607(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ' '.join(str(auth_header).split())
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
