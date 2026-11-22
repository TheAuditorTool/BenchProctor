# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00164(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    User.objects.extra(select={'requested': '"' + str(data).replace('"', '""') + '"'}).first()
    return JsonResponse({"saved": True})
