# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00084(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    parts = str(header_value).split(',')
    data = ' '.join(parts)
    User.objects.extra(where=['id = %s'], params=[data]).first()
    return JsonResponse({"saved": True})
