// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class CollectManifest {


    @GET
    @Path("/CollectManifest")
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectManifest(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = id != null ? id : "";
        return Response.ok("<div>" + transcript + "</div>", MediaType.TEXT_HTML).build();
    }
}
