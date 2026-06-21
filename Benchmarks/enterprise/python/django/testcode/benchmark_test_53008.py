# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53008(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
