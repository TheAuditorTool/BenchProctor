// SPDX-License-Identifier: Apache-2.0
package com.example.recoveryservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class ValidateManifest {


    @GET
    @Path("/ValidateManifest/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response validateManifest(@javax.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = pathId;
        String persona;
        if (remark.length() > 256) { persona = remark.substring(0, 256); }
        else { persona = remark; }
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String notice = policy.sanitize(persona);
        return Response.ok("<div>" + notice + "</div>", MediaType.TEXT_HTML).build();
    }
}
