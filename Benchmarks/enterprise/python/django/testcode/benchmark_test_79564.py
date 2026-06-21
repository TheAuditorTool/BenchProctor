# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79564(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(referer_value)})
