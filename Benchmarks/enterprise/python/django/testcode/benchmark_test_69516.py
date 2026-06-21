# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69516(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
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
