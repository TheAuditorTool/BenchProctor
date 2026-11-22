# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse


@csrf_exempt
def build_policy(request):
    heading = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(heading)
    return HttpResponse(mark_safe('<div>' + str(handshake) + '</div>'))
