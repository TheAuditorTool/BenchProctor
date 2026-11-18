# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00157(request):
    raw_body = request.body.decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    User.objects.filter(id=data).first()
    return JsonResponse({"saved": True})
