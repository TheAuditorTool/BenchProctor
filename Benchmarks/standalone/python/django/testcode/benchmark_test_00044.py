# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00044(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % str(ua_value)
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _coerced
    matches = len(User.objects.raw('SELECT * FROM users WHERE id = ' + str(processed)))
    return JsonResponse({'matches': matches}, status=200)
