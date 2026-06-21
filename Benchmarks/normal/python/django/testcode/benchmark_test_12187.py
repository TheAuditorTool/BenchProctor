# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64


def BenchmarkTest12187(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
