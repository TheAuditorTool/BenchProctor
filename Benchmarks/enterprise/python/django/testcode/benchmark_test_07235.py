# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07235(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
