// SPDX-License-Identifier: Apache-2.0
package com.example.mappingstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class CollectReport {


    @POST
    @Path("/CollectReport/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectReport(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String snippet = java.util.Optional.ofNullable(commentText).orElse("");
        String handshake;
        if (snippet.length() > 256) { handshake = snippet.substring(0, 256); }
        else { handshake = snippet; }
        if (!handshake.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { return Response.status(400).build(); }
        return Response.ok("<div>" + handshake + "</div>", MediaType.TEXT_HTML).build();
    }
}
