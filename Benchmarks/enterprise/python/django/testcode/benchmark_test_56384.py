# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest56384(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = full_path
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
