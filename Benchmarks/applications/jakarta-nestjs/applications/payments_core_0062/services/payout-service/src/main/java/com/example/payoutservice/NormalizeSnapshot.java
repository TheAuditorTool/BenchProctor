// SPDX-License-Identifier: Apache-2.0
package com.example.payoutservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class NormalizeSnapshot {


    @GET
    @Path("/NormalizeSnapshot")
    @Produces(MediaType.APPLICATION_JSON)
    public Response normalizeSnapshot(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headline = id != null ? id : "";
        byte[] hexBytes = new byte[headline.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(headline.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String disbursement = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(disbursement)) { return Response.status(403).build(); }
        String remittance = disbursement;
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + remittance}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
