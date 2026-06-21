# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68184(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
