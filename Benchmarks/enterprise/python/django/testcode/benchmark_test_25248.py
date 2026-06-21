# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25248(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
