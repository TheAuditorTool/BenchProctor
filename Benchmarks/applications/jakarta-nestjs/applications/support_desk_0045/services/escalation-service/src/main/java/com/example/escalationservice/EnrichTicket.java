// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class EnrichTicket {


    @POST
    @Path("/EnrichTicket")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response enrichTicket(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = rawBody != null ? rawBody : "";
        java.util.Properties holder = new java.util.Properties();
        holder.setProperty("value", remark);
        String inquiry = holder.getProperty("value", "");
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(inquiry)) { return Response.status(403).build(); }
        String grievance = "/var/app/data/" + inquiry;
        Files.write(Paths.get(grievance), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
