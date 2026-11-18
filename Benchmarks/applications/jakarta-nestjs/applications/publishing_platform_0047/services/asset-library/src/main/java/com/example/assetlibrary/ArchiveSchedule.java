// SPDX-License-Identifier: Apache-2.0
package com.example.assetlibrary;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class ArchiveSchedule {


    @GET
    @Path("/ArchiveSchedule")
    @Produces(MediaType.APPLICATION_JSON)
    public Response archiveSchedule(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String synopsis = referer != null ? referer : "";
        java.util.function.Supplier<String> valueSupplier = () -> synopsis.strip();
        String byline = valueSupplier.get();
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + byline});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
