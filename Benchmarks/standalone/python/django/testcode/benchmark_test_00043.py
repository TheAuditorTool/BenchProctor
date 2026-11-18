# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00043(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % (ua_value,)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = full_path
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
