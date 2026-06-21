# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import base64


def BenchmarkTest59075(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
