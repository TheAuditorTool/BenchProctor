# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67718(request):
    xml_value = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
