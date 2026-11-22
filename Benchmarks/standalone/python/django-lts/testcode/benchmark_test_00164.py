# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00164(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % (auth_header,)
    User.objects.extra(where=["name = '" + str(data) + "'"]).first()
    return JsonResponse({"saved": True})
