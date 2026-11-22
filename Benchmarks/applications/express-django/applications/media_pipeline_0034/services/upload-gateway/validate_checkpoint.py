# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


@csrf_exempt
def validate_checkpoint(request):
    synopsis = request.POST.get('field', '')
    if synopsis:
        rendition = synopsis
    else:
        rendition = ''
    return HttpResponse(Template('{{ value }}').render(Context({'value': rendition})))
