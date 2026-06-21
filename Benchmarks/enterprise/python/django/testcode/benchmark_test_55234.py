# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55234(request):
    raw_body = request.body.decode('utf-8')
    return JsonResponse({'error': str(raw_body), 'stack': repr(locals())}, status=500)
