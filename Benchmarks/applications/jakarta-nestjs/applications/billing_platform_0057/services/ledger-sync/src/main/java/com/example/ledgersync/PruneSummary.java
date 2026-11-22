// SPDX-License-Identifier: Apache-2.0
package com.example.ledgersync;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class PruneSummary {


    @GET
    @Path("/PruneSummary/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response pruneSummary(@javax.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = pathId;
        String remittance;
        if (caption.length() > 256) { remittance = caption.substring(0, 256); }
        else { remittance = caption; }
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String dunning = policy.sanitize(remittance);
        return Response.ok("<div>" + dunning + "</div>", MediaType.TEXT_HTML).build();
    }
}
