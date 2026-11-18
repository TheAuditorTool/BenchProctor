# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00453(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = str(ua_value).split(',')
    data = ' '.join(parts)
    User.objects.filter(id=data).first()
    return JsonResponse({"saved": True})
