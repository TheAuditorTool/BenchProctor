# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest35245(request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return JsonResponse({'error': 'invalid file type'}, status=400)
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
