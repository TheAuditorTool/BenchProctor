// SPDX-License-Identifier: Apache-2.0
package com.example.samplingconfig;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class AuditManifest {


    @POST
    @Path("/AuditManifest/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response auditManifest(@jakarta.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String note = java.util.Optional.ofNullable(commentText).orElse("");
        String gauge;
        if (note.length() > 256) { gauge = note.substring(0, 256); }
        else { gauge = note; }
        if (!gauge.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { return Response.status(400).build(); }
        return Response.ok("<div>" + gauge + "</div>", MediaType.TEXT_HTML).build();
    }
}
