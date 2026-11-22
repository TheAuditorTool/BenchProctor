// SPDX-License-Identifier: Apache-2.0
package com.example.cyclecount;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class ArchiveLedger {


    @GET
    @Path("/ArchiveLedger")
    @Produces(MediaType.APPLICATION_JSON)
    public Response archiveLedger(@javax.validation.constraints.Size(max = 4096) @CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String memo = sessionToken != null ? sessionToken : "";
        String backorder;
        if (memo.length() > 256) { backorder = memo.substring(0, 256); }
        else { backorder = memo; }
        java.nio.file.Path base = java.nio.file.Paths.get("/var/app/data");
        java.nio.file.Path resolved = base.resolve(backorder).normalize();
        if (!resolved.startsWith(base)) { return Response.status(403).build(); }
        String restock = resolved.toString();
        String content = Files.readString(Paths.get(restock), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
