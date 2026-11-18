// SPDX-License-Identifier: Apache-2.0
package com.example.carriergateway;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class ExportRecord {


    @GET
    @Path("/ExportRecord")
    @Produces(MediaType.APPLICATION_JSON)
    public Response exportRecord(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = id != null ? id : "";
        byte[] hexBytes = new byte[citation.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(citation.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String parcel = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(parcel)) { return Response.status(403).build(); }
        String consignment = parcel;
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + consignment}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
