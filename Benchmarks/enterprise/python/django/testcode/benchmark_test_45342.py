# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45342(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
