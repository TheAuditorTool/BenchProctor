# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00083(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = str(referer_value).split(',')
    data = ' '.join(parts)
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _coerced
    User.objects.extra(where=['id = ' + str(processed)]).first()
    return JsonResponse({"saved": True})
