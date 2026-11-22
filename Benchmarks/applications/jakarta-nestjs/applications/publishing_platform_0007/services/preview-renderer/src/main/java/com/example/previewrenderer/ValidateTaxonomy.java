// SPDX-License-Identifier: Apache-2.0
package com.example.previewrenderer;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class ValidateTaxonomy {


    @POST
    @Path("/ValidateTaxonomy")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response validateTaxonomy(@javax.validation.constraints.Size(max = 4096) String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = rawBody != null ? rawBody : "";
        java.util.Properties store = new java.util.Properties();
        store.setProperty("value", remark);
        String byline = store.getProperty("value", "");
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(byline)) { return Response.status(403).build(); }
        String addendum = "/var/app/data/" + byline;
        Files.write(Paths.get(addendum), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
