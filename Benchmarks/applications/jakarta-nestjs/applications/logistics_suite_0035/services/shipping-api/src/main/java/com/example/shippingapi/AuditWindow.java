// SPDX-License-Identifier: Apache-2.0
package com.example.shippingapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class AuditWindow {


    @GET
    @Path("/AuditWindow/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response auditWindow(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String phrase = pathId;
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String parcel = transform.apply(phrase);
        return Response.ok("<div>" + parcel + "</div>", MediaType.TEXT_HTML).build();
    }
}
