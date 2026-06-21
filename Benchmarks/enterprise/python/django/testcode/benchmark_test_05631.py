# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05631(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
