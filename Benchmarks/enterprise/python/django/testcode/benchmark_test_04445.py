# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest04445(request):
    xml_value = request.body.decode('utf-8')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(xml_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = xml_value
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(processed).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JsonResponse({'is_admin': profile.is_admin}, status=200)
