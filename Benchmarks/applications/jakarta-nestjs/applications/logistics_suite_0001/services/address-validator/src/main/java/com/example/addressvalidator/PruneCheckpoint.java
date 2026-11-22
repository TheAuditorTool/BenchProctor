// SPDX-License-Identifier: Apache-2.0
package com.example.addressvalidator;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class PruneCheckpoint {


    @GET
    @Path("/PruneCheckpoint/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response pruneCheckpoint(@javax.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String quotation = pathId;
        String parcel;
        if (quotation.length() > 256) { parcel = quotation.substring(0, 256); }
        else { parcel = quotation; }
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String consignment = policy.sanitize(parcel);
        return Response.ok("<div>" + consignment + "</div>", MediaType.TEXT_HTML).build();
    }
}
