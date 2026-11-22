# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00204(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = bytes.fromhex(file_value).decode('utf-8', 'ignore')
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _coerced
    User.objects.extra(where=['id = ' + str(processed)]).first()
    return JsonResponse({"saved": True})
