# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78263(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header:.200s}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
