# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest12434(request):
    xml_value = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
