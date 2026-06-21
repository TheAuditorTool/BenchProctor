# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63242(request, path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(data).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JsonResponse({'is_admin': profile.is_admin}, status=200)
