// SPDX-License-Identifier: Apache-2.0
package com.example.jobservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class MergeReport {


    @GET
    @Path("/MergeReport/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response mergeReport(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = pathId;
        String persona;
        if (remark.length() > 256) { persona = remark.substring(0, 256); }
        else { persona = remark; }
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String handshake = policy.sanitize(persona);
        return Response.ok("<div>" + handshake + "</div>", MediaType.TEXT_HTML).build();
    }
}
