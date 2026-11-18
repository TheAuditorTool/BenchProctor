// SPDX-License-Identifier: Apache-2.0
package com.example.auditlog;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class ExportRoster {


    @GET
    @Path("/ExportRoster")
    @Produces(MediaType.APPLICATION_JSON)
    public Response exportRoster(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String tagline = authorization != null ? authorization : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String persona = transform.apply(tagline);
        return Response.ok("<div>" + persona + "</div>", MediaType.TEXT_HTML).build();
    }
}
