# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39799(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
