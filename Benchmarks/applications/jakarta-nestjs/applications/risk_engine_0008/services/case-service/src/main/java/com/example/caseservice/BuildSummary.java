// SPDX-License-Identifier: Apache-2.0
package com.example.caseservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class BuildSummary {


    @GET
    @Path("/BuildSummary")
    @Produces(MediaType.APPLICATION_JSON)
    public Response buildSummary(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String synopsis = referer != null ? referer : "";
        java.util.function.Supplier<String> valueSupplier = () -> synopsis.strip();
        String verdict = valueSupplier.get();
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + verdict});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
