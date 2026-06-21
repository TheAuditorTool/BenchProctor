# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest22848(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    kind = 'json' if str(prop_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = prop_value
            data = parsed
        case _:
            data = prop_value
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
