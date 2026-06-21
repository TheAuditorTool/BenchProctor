# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest62741(request):
    user_id = request.GET.get('id', '')
    data = default_blank(user_id)
    checked_path = os.path.normpath(data)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(checked_path))
    return JsonResponse({"saved": True})
