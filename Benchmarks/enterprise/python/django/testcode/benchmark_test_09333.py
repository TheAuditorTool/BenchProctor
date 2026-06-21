# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09333(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(processed).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JsonResponse({'is_admin': profile.is_admin}, status=200)
