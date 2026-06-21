# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36237(request):
    xml_value = request.body.decode('utf-8')
    allowed_fields = {'name', 'email', 'bio'}
    if str(xml_value).split('=', 1)[0] not in allowed_fields:
        return JsonResponse({'error': 'field not allowed'}, status=400)
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
