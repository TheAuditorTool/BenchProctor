// SPDX-License-Identifier: Apache-2.0
package com.example.logshipper;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class LoadSummary {


    @GET
    @Path("/LoadSummary")
    @Produces(MediaType.APPLICATION_JSON)
    public Response loadSummary(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = id != null ? id : "";
        byte[] hexBytes = new byte[summary.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(summary.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String gauge = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(gauge)) { return Response.status(403).build(); }
        String cohort = gauge;
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + cohort}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
