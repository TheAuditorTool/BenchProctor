// SPDX-License-Identifier: Apache-2.0
package com.example.assetlibrary;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class MergeConfig {


    @POST
    @Path("/MergeConfig")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response mergeConfig(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String heading = rawBody != null ? rawBody : "";
        String addendum;
        if (heading.length() > 256) { addendum = heading.substring(0, 256); }
        else { addendum = heading; }
        Files.write(Paths.get("/var/uploads/" + addendum), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
