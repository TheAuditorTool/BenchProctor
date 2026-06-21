# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def normalise_input(value):
    return value.strip()

def BenchmarkTest58554(request):
    xml_value = request.body.decode('utf-8')
    data = normalise_input(xml_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
