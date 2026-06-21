# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest65981(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
