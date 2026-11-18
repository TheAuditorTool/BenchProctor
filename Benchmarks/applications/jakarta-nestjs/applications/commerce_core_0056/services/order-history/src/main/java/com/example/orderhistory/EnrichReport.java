// SPDX-License-Identifier: Apache-2.0
package com.example.orderhistory;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class EnrichReport {


    @POST
    @Path("/EnrichReport/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response enrichReport(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = java.util.Optional.ofNullable(commentText).orElse("");
        String backorder;
        if (citation.length() > 256) { backorder = citation.substring(0, 256); }
        else { backorder = citation; }
        if (!backorder.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { return Response.status(400).build(); }
        return Response.ok("<div>" + backorder + "</div>", MediaType.TEXT_HTML).build();
    }
}
