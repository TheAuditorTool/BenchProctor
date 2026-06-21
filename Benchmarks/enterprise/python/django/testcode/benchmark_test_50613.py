# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest50613(request):
    user_id = request.GET.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(user_id)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = user_id
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(processed).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JsonResponse({'is_admin': profile.is_admin}, status=200)
