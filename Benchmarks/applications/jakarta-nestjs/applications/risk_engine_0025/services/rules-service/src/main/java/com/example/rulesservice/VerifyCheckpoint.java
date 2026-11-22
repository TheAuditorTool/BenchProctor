// SPDX-License-Identifier: Apache-2.0
package com.example.rulesservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class VerifyCheckpoint {


    @GET
    @Path("/VerifyCheckpoint")
    @Produces(MediaType.APPLICATION_JSON)
    public Response verifyCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String excerpt = xForwardedFor != null ? xForwardedFor : "";
        String prefix = excerpt.length() > 0 ? excerpt.substring(0, 1).toLowerCase() : "";
        String verdict;
        switch (prefix) {
            case "h": verdict = excerpt.toLowerCase(); break;
            case "f": verdict = excerpt.toUpperCase(); break;
            default: verdict = excerpt.strip(); break;
        }
        Files.write(Paths.get("/var/uploads/" + verdict), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
