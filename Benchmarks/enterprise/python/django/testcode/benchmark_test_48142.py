# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48142(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
