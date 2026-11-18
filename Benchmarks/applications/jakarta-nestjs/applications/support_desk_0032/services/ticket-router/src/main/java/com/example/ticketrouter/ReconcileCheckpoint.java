// SPDX-License-Identifier: Apache-2.0
package com.example.ticketrouter;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class ReconcileCheckpoint {


    @GET
    @Path("/ReconcileCheckpoint/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response reconcileCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String note = pathId;
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String inquiry = transform.apply(note);
        return Response.ok("<div>" + inquiry + "</div>", MediaType.TEXT_HTML).build();
    }
}
