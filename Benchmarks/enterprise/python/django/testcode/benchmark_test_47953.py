# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import requests
import ast


def BenchmarkTest47953(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    try:
        data = str(ast.literal_eval(api_value))
    except (ValueError, SyntaxError):
        data = api_value
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return JsonResponse({'error': 'invalid file type'}, status=400)
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
