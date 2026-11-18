// SPDX-License-Identifier: Apache-2.0
package com.example.presencehub;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class NormalizeSnapshot {


    @GET
    @Path("/NormalizeSnapshot")
    @Produces(MediaType.APPLICATION_JSON)
    public Response normalizeSnapshot(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String preface = id != null ? id : "";
        return Response.ok("<div>" + preface + "</div>", MediaType.TEXT_HTML).build();
    }
}
