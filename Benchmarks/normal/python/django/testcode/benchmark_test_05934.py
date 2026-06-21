# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest05934(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
