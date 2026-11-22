// SPDX-License-Identifier: Apache-2.0
package com.example.revisionstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class EnrichArticle {


    @GET
    @Path("/EnrichArticle/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response enrichArticle(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = pathId;
        String addendum;
        if (transcript.length() > 256) { addendum = transcript.substring(0, 256); }
        else { addendum = transcript; }
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String byline = policy.sanitize(addendum);
        return Response.ok("<div>" + byline + "</div>", MediaType.TEXT_HTML).build();
    }
}
