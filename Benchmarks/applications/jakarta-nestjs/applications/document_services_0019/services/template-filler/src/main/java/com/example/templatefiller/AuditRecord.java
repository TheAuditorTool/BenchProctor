// SPDX-License-Identifier: Apache-2.0
package com.example.templatefiller;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class AuditRecord {


    @GET
    @Path("/AuditRecord")
    @Produces(MediaType.APPLICATION_JSON)
    public Response auditRecord(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String passage = authorization != null ? authorization : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String dossier = transform.apply(passage);
        return Response.ok("<div>" + dossier + "</div>", MediaType.TEXT_HTML).build();
    }
}
