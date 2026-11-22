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
public class CompactSummary {


    @POST
    @Path("/CompactSummary")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactSummary(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String subject = rawBody != null ? rawBody : "";
        String voucher;
        if (subject.length() > 256) { voucher = subject.substring(0, 256); }
        else { voucher = subject; }
        Files.write(Paths.get("/var/uploads/" + voucher), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
