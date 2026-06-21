# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42823(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
