# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import base64


def BenchmarkTest70594(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
