# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71691(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % (auth_header,)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
