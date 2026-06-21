# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33120(request):
    xml_value = request.body.decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
