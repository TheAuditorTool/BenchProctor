# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest00408(request):
    multipart_value = request.POST.get('multipart_field', '')
    kind = 'json' if str(multipart_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(multipart_value).strip()
        case _:
            data = str(multipart_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
