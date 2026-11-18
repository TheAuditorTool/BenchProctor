// SPDX-License-Identifier: Apache-2.0
package com.example.presencehub;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class PublishSchedule {


    @POST
    @Path("/PublishSchedule/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishSchedule(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String preface = java.util.Optional.ofNullable(commentText).orElse("");
        String remark;
        if (preface.length() > 256) { remark = preface.substring(0, 256); }
        else { remark = preface; }
        if (!remark.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { return Response.status(400).build(); }
        return Response.ok("<div>" + remark + "</div>", MediaType.TEXT_HTML).build();
    }
}
