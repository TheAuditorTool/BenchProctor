# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


def BenchmarkTest23697(request):
    multipart_value = request.POST.get('multipart_field', '')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(multipart_value))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
