// SPDX-License-Identifier: Apache-2.0
package com.example.macroservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class ExportReport {


    @POST
    @Path("/ExportReport/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response exportReport(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String phrase = java.util.Optional.ofNullable(commentText).orElse("");
        String inquiry;
        if (phrase.length() > 256) { inquiry = phrase.substring(0, 256); }
        else { inquiry = phrase; }
        if (!inquiry.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { return Response.status(400).build(); }
        return Response.ok("<div>" + inquiry + "</div>", MediaType.TEXT_HTML).build();
    }
}
