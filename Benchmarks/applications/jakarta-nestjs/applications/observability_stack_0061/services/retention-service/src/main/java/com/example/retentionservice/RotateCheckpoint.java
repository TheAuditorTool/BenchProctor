// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class RotateCheckpoint {


    @GET
    @Path("/RotateCheckpoint")
    @Produces(MediaType.APPLICATION_JSON)
    public Response rotateCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = id != null ? id : "";
        return Response.ok("<div>" + headline + "</div>", MediaType.TEXT_HTML).build();
    }
}
