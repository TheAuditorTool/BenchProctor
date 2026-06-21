# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest26834(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not header_value.lower().endswith(allowed_ext):
        return JsonResponse({'error': 'invalid file type'}, status=400)
    entry_file = os.path.basename(header_value)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
