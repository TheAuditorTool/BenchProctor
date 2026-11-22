// SPDX-License-Identifier: Apache-2.0
package com.example.samplingconfig;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class AnnotateReport {


    @GET
    @Path("/AnnotateReport")
    @Produces(MediaType.APPLICATION_JSON)
    public Response annotateReport(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = referer != null ? referer : "";
        java.util.Properties store = new java.util.Properties();
        store.setProperty("value", remark);
        String gauge = store.getProperty("value", "");
        String content = Files.readString(Paths.get("/var/app/data/" + gauge), java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
