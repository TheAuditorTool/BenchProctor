// SPDX-License-Identifier: Apache-2.0
package com.example.supplierfeed;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class FormatBundle {


    @POST
    @Path("/FormatBundle/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response formatBundle(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = java.util.Optional.ofNullable(commentText).orElse("");
        String backorder = citation.replace("\u0000", "");
        return Response.ok("<div>" + backorder + "</div>", MediaType.TEXT_HTML).build();
    }
}
