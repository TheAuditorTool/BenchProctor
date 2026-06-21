# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest56888(request):
    xml_value = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
