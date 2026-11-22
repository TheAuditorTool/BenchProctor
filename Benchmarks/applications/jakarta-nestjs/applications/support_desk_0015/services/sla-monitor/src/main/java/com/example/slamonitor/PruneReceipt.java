// SPDX-License-Identifier: Apache-2.0
package com.example.slamonitor;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class PruneReceipt {


    @POST
    @Path("/PruneReceipt")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response pruneReceipt(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String phrase = rawBody != null ? rawBody : "";
        String grievance;
        if (phrase.length() > 256) { grievance = phrase.substring(0, 256); }
        else { grievance = phrase; }
        Files.write(Paths.get("/var/uploads/" + grievance), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
