// SPDX-License-Identifier: Apache-2.0
package com.example.transformservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class ReconcileLedger {


    @GET
    @Path("/ReconcileLedger")
    @Produces(MediaType.APPLICATION_JSON)
    public Response reconcileLedger(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = java.util.Optional.ofNullable((String) request.getAttribute("uploadName")).orElse("");
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String handshake = transform.apply(caption);
        Files.delete(Paths.get("/var/app/data/" + handshake));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
