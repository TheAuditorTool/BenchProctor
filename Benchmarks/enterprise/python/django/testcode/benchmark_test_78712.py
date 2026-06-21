# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78712(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
