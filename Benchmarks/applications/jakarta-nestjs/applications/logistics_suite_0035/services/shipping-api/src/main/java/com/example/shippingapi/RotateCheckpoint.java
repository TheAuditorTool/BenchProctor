// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class RotateCheckpoint {


    @POST
    @Path("/RotateCheckpoint/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response rotateCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String phrase = java.util.Optional.ofNullable(commentText).orElse("");
        String parcel;
        if (phrase.length() > 256) { parcel = phrase.substring(0, 256); }
        else { parcel = phrase; }
        if (!parcel.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { return Response.status(400).build(); }
        return Response.ok("<div>" + parcel + "</div>", MediaType.TEXT_HTML).build();
    }
}
