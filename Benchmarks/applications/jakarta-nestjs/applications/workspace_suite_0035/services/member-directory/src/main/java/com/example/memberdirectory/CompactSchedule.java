// SPDX-License-Identifier: Apache-2.0
package com.example.memberdirectory;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class CompactSchedule {


    @GET
    @Path("/CompactSchedule/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactSchedule(@javax.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String paragraph = pathId;
        String wording;
        if (paragraph.length() > 256) { wording = paragraph.substring(0, 256); }
        else { wording = paragraph; }
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String transcript = policy.sanitize(wording);
        return Response.ok("<div>" + transcript + "</div>", MediaType.TEXT_HTML).build();
    }
}
