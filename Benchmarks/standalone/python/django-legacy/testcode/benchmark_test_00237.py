# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00237(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    reader = make_reader(auth_header)
    data = reader()
    User.objects.filter(id=data).first()
    return JsonResponse({"saved": True})
