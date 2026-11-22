// SPDX-License-Identifier: Apache-2.0
package com.example.fulfillmentservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class FormatCart {

    record FormData(String payload) {}

    @GET
    @Path("/FormatCart")
    @Produces(MediaType.APPLICATION_JSON)
    public Response formatCart(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subject = referer != null ? referer : "";
        FormData payload = new FormData(subject);
        String voucher = payload.payload();
        if (!voucher.matches("^[a-zA-Z0-9 _.#~\\-]+$")) { return Response.status(400).build(); }
        Files.write(Paths.get("/var/uploads/" + voucher), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
