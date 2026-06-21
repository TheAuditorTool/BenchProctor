# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40785(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(processed).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JsonResponse({'is_admin': profile.is_admin}, status=200)
