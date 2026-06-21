# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12735(request):
    xml_value = request.body.decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
