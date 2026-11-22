// SPDX-License-Identifier: Apache-2.0
package com.example.catalogapi;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class LoadBatch {


    @GET
    @Path("/LoadBatch")
    @Produces(MediaType.APPLICATION_JSON)
    public Response loadBatch(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String excerpt = referer != null ? referer : "";
        String restock;
        if (excerpt.length() > 256) { restock = excerpt.substring(0, 256); }
        else { restock = excerpt; }
        String backorder = restock.matches("^(status|info|list|show)$") ? restock : "status";
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + backorder});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
