# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00059(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    User.objects.filter(id=data).first()
    return JsonResponse({"saved": True})
