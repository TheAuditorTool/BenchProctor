# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21536(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header:.200s}'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
