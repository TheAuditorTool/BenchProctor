# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11776(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
