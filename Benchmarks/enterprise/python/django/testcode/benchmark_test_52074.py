# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52074(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
