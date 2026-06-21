# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest73815(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not auth_header.lower().endswith(allowed_ext):
        return JsonResponse({'error': 'invalid file type'}, status=400)
    entry_file = os.path.basename(auth_header)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
