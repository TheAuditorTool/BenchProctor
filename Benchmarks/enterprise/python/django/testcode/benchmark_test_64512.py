# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
from urllib.parse import unquote


def BenchmarkTest64512(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
