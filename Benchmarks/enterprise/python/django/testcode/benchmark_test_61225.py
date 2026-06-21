# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import os


def BenchmarkTest61225(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
