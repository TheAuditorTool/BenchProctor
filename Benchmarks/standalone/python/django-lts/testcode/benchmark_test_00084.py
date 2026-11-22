# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00084(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    matches = len(User.objects.raw("SELECT * FROM users WHERE name = '" + str(data) + "'"))
    return JsonResponse({'matches': matches}, status=200)
