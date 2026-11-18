# SPDX-License-Identifier: Apache-2.0
import os
from django.http import HttpResponse


def BenchmarkTest00280(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(auth_header).strip()
        case _:
            data = str(auth_header)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
