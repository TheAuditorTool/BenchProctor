// SPDX-License-Identifier: Apache-2.0
package com.example.decisionlog;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class NormalizeBatch {


    @POST
    @Path("/NormalizeBatch")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response normalizeBatch(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String memo = rawBody != null ? rawBody : "";
        java.util.Properties store = new java.util.Properties();
        store.setProperty("value", memo);
        String verdict = store.getProperty("value", "");
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(verdict)) { return Response.status(403).build(); }
        String grievance = "/var/app/data/" + verdict;
        Files.write(Paths.get(grievance), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
