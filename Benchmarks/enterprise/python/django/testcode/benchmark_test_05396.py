# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05396(request):
    multipart_value = request.POST.get('multipart_field', '')
    kind = 'json' if str(multipart_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = multipart_value
            data = parsed
        case _:
            data = multipart_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
