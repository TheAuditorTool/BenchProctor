// SPDX-License-Identifier: Apache-2.0
package com.example.trackingservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class ExportBundle {


    @GET
    @Path("/ExportBundle/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response exportBundle(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = pathId;
        String consignment;
        if (caption.length() > 256) { consignment = caption.substring(0, 256); }
        else { consignment = caption; }
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String parcel = policy.sanitize(consignment);
        return Response.ok("<div>" + parcel + "</div>", MediaType.TEXT_HTML).build();
    }
}
