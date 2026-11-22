# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00027(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = '%s' % str(config_value)
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _coerced
    User.objects.extra(where=['id = ' + str(processed)]).first()
    return JsonResponse({"saved": True})
