# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile
import os
from types import SimpleNamespace


def BenchmarkTest09951(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
