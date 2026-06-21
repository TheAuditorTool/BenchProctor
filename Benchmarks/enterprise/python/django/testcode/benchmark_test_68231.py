# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68231(request):
    multipart_value = request.POST.get('multipart_field', '')
    kind = 'json' if str(multipart_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = multipart_value
            data = parsed
        case _:
            data = multipart_value
    eval(str(data))
    return JsonResponse({"saved": True})
