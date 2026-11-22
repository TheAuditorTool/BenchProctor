// SPDX-License-Identifier: Apache-2.0
package com.example.signatureverifier;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class RotateLedger {


    @GET
    @Path("/RotateLedger/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response rotateLedger(@javax.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = pathId;
        String handshake;
        if (summary.length() > 256) { handshake = summary.substring(0, 256); }
        else { handshake = summary; }
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String paragraph = policy.sanitize(handshake);
        return Response.ok("<div>" + paragraph + "</div>", MediaType.TEXT_HTML).build();
    }
}
