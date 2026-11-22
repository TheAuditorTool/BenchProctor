# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.contrib.auth.models import User


def BenchmarkTest00219(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    matches = len(User.objects.raw("SELECT * FROM users WHERE name = '" + str(data) + "'"))
    return JsonResponse({'matches': matches}, status=200)
