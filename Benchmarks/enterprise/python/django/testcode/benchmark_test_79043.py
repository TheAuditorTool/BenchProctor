# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
import tempfile


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest79043(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return JsonResponse({"saved": True})
