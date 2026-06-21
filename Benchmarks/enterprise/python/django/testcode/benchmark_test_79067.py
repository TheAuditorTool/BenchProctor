# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest79067(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = default_blank(json_value)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
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
