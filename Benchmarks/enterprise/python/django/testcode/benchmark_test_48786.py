# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import requests


def BenchmarkTest48786(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not api_value.lower().endswith(allowed_ext):
        return JsonResponse({'error': 'invalid file type'}, status=400)
    entry_file = os.path.basename(api_value)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
