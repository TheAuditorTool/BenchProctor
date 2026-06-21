# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest50590(request):
    cookie_value = request.COOKIES.get('session_token', '')
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not cookie_value.lower().endswith(allowed_ext):
        return JsonResponse({'error': 'invalid file type'}, status=400)
    entry_file = os.path.basename(cookie_value)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
