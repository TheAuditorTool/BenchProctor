# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47601(request):
    upload_name = request.FILES['upload'].name
    kind = 'json' if str(upload_name).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = upload_name
            data = parsed
        case _:
            data = upload_name
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
