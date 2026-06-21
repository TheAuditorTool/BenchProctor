# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import base64
from django.http import HttpResponse


def BenchmarkTest68532(request):
    raw_body = request.body.decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = full_path
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
