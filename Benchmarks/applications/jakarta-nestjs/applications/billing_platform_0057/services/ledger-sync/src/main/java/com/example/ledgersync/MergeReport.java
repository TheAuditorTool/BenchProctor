// SPDX-License-Identifier: Apache-2.0
package com.example.ledgersync;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class MergeReport {


    @GET
    @Path("/MergeReport")
    @Produces(MediaType.APPLICATION_JSON)
    public Response mergeReport(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = xForwardedFor != null ? xForwardedFor : "";
        String prefix = caption.length() > 0 ? caption.substring(0, 1).toLowerCase() : "";
        String remittance;
        switch (prefix) {
            case "h": remittance = caption.toLowerCase(); break;
            case "f": remittance = caption.toUpperCase(); break;
            default: remittance = caption.strip(); break;
        }
        Files.write(Paths.get("/var/uploads/" + remittance), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
