# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest71345(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = default_blank(multipart_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return JsonResponse({"saved": True})
