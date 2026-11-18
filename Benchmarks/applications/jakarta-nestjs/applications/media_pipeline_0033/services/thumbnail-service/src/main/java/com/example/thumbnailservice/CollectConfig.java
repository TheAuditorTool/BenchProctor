// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class CollectConfig {


    @GET
    @Path("/CollectConfig")
    @Produces(MediaType.APPLICATION_JSON)
    public Response collectConfig(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String transcript = referer != null ? referer : "";
        java.util.function.Supplier<String> valueSupplier = () -> transcript.strip();
        String rendition = valueSupplier.get();
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + rendition});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
