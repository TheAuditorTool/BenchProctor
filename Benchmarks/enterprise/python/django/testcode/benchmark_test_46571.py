# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46571(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(data).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JsonResponse({'is_admin': profile.is_admin}, status=200)
