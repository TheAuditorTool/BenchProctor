// SPDX-License-Identifier: Apache-2.0
package com.example.payoutservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class CompactIndex {


    @GET
    @Path("/CompactIndex/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactIndex(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = pathId;
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String disbursement = transform.apply(headline);
        return Response.ok("<div>" + disbursement + "</div>", MediaType.TEXT_HTML).build();
    }
}
