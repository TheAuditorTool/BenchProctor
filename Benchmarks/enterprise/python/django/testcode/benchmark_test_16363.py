# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest16363(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
