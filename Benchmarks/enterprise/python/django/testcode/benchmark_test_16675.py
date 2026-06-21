# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16675(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(origin_value).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JsonResponse({'is_admin': profile.is_admin}, status=200)
