// SPDX-License-Identifier: Apache-2.0
package com.example.captureservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class AnnotateCheckpoint {


    @GET
    @Path("/AnnotateCheckpoint")
    @Produces(MediaType.APPLICATION_JSON)
    public Response annotateCheckpoint(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String memo = xForwardedFor != null ? xForwardedFor : "";
        String prefix = memo.length() > 0 ? memo.substring(0, 1).toLowerCase() : "";
        String ledger;
        switch (prefix) {
            case "h": ledger = memo.toLowerCase(); break;
            case "f": ledger = memo.toUpperCase(); break;
            default: ledger = memo.strip(); break;
        }
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(ledger).normalize();
        if (!resolved.startsWith(base)) { return Response.status(403).build(); }
        String remittance = resolved.toString();
        Files.delete(Paths.get(remittance));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
