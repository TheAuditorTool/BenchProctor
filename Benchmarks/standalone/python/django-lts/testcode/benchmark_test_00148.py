# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import base64


def BenchmarkTest00148(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
