# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35821(request):
    xml_value = request.body.decode('utf-8')
    kind = 'json' if str(xml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = xml_value
            data = parsed
        case _:
            data = xml_value
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
