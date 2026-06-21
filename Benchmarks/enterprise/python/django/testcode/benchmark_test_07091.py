# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07091(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(data).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JsonResponse({'is_admin': profile.is_admin}, status=200)
