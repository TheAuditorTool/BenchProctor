# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71127(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % (auth_header,)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
