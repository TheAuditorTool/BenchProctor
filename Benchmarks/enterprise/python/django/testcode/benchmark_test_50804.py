# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import base64


def BenchmarkTest50804(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return JsonResponse({"saved": True})
