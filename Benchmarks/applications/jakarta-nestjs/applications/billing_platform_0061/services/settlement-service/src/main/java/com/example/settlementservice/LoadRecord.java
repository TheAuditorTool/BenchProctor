// SPDX-License-Identifier: Apache-2.0
package com.example.settlementservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class LoadRecord {


    @GET
    @Path("/LoadRecord")
    @Produces(MediaType.APPLICATION_JSON)
    public Response loadRecord(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = referer != null ? referer : "";
        java.util.Properties container = new java.util.Properties();
        container.setProperty("value", footnote);
        String remittance = container.getProperty("value", "");
        String content = Files.readString(Paths.get("/var/app/data/" + remittance), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
