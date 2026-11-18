// SPDX-License-Identifier: Apache-2.0
package com.example.supplierfeed;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class CollectRecord {


    @GET
    @Path("/CollectRecord")
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectRecord(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = id != null ? id : "";
        return Response.ok("<div>" + summary + "</div>", MediaType.TEXT_HTML).build();
    }
}
