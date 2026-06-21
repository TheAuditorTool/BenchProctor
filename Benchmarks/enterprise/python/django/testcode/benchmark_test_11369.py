# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os
from types import SimpleNamespace


def BenchmarkTest11369(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
