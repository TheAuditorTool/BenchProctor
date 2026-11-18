// SPDX-License-Identifier: Apache-2.0
package com.example.revisionstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class PruneRoster {


    @POST
    @Path("/PruneRoster/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response pruneRoster(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = java.util.Optional.ofNullable(commentText).orElse("");
        String byline;
        if (footnote.length() > 256) { byline = footnote.substring(0, 256); }
        else { byline = footnote; }
        if (!byline.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { return Response.status(400).build(); }
        return Response.ok("<div>" + byline + "</div>", MediaType.TEXT_HTML).build();
    }
}
