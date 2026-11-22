# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00107(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = auth_header if auth_header else 'default'
    matches = len(User.objects.raw("SELECT * FROM users WHERE name = '" + str(data) + "'"))
    return JsonResponse({'matches': matches}, status=200)
