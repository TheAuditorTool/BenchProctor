# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00182(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    kind = 'json' if str(forwarded_ip).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(forwarded_ip).strip()
        case _:
            data = str(forwarded_ip)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
