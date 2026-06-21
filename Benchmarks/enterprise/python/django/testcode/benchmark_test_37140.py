# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest37140(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = json_value if json_value else 'default'
    allowed_fields = {'name', 'email', 'bio'}
    if str(data).split('=', 1)[0] not in allowed_fields:
        return JsonResponse({'error': 'field not allowed'}, status=400)
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
