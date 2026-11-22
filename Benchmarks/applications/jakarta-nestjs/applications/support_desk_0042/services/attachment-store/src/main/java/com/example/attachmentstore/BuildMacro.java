// SPDX-License-Identifier: Apache-2.0
package com.example.attachmentstore;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BuildMacro {


    @GET
    @Path("/BuildMacro")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildMacro(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String blurb = java.util.Optional.ofNullable((String) request.getAttribute("uploadName")).orElse("");
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String inquiry = transform.apply(blurb);
        Files.delete(Paths.get("/var/app/data/" + inquiry));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
