# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01143(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
