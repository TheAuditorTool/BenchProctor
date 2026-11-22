// SPDX-License-Identifier: Apache-2.0
package com.example.archivestore;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class FormatRedaction {


    @GET
    @Path("/FormatRedaction/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response formatRedaction(@javax.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String phrase = pathId;
        String dossier;
        if (phrase.length() > 256) { dossier = phrase.substring(0, 256); }
        else { dossier = phrase; }
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String addendum = policy.sanitize(dossier);
        return Response.ok("<div>" + addendum + "</div>", MediaType.TEXT_HTML).build();
    }
}
