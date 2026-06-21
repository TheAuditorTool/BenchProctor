# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05020(request, path_param):
    path_value = path_param
    processed = 'true' if str(path_value).lower() in ('true', '1', 'yes', 'on') else 'false'
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(processed).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JsonResponse({'is_admin': profile.is_admin}, status=200)
