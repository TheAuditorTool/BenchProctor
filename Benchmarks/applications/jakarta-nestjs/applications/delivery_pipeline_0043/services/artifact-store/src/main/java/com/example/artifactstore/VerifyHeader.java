// SPDX-License-Identifier: Apache-2.0
package com.example.artifactstore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class VerifyHeader {


    @GET
    @Path("/VerifyHeader")
    @Produces(MediaType.APPLICATION_JSON)
    public Response verifyHeader(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = java.util.Optional.ofNullable((String) request.getAttribute("uploadName")).orElse("");
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String note = transform.apply(remark);
        Files.delete(Paths.get("/var/app/data/" + note));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
