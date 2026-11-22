# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00038(request):
    field_value = request.POST.get('field', '')
    data = str(field_value).replace('\x00', '')
    User.objects.extra(where=['id = %s'], params=[data]).first()
    return JsonResponse({"saved": True})
