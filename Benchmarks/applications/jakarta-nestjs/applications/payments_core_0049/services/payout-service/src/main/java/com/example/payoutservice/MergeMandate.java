// SPDX-License-Identifier: Apache-2.0
package com.example.payoutservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class MergeMandate {


    @POST
    @Path("/MergeMandate")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response mergeMandate(@jakarta.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = rawBody != null ? rawBody : "";
        String disbursement;
        if (headline.length() > 256) { disbursement = headline.substring(0, 256); }
        else { disbursement = headline; }
        Files.write(Paths.get("/var/uploads/" + disbursement), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
