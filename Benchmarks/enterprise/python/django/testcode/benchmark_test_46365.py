# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
import tempfile


def BenchmarkTest46365(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
