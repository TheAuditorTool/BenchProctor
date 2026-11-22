# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00219(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    if header_value:
        data = header_value
    else:
        data = ''
    User.objects.filter(id=data).first()
    return JsonResponse({"saved": True})
