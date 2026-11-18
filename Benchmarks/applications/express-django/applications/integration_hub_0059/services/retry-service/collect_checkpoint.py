# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def collect_checkpoint(request):
    synopsis = request.body.decode('utf-8')
    handshake = synopsis if synopsis else 'default'
    memo = bleach.clean(handshake)
    return HttpResponse(mark_safe('<div>' + str(memo) + '</div>'))
