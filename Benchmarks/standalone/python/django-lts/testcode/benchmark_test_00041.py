# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from pathlib import Path


def BenchmarkTest00041(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '{}'.format(cookie_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    Path(checked_path).write_text('data')
    return JsonResponse({"saved": True})
