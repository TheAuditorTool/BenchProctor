# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26481(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = ' '.join(str(forwarded_ip).split())
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
