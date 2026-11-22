// SPDX-License-Identifier: Apache-2.0
package com.example.returnsservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class RotateFulfillment {

    record FormData(String payload) {}

    @GET
    @Path("/RotateFulfillment")
    @Produces(MediaType.APPLICATION_JSON)
    public Response rotateFulfillment(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String notice = referer != null ? referer : "";
        FormData payload = new FormData(notice);
        String backorder = payload.payload();
        if (!backorder.matches("^[a-zA-Z0-9 _.#~\\-]+$")) { return Response.status(400).build(); }
        Files.write(Paths.get("/var/uploads/" + backorder), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
