// SPDX-License-Identifier: Apache-2.0
package com.example.logshipper;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class ResolveWindow {


    @GET
    @Path("/ResolveWindow")
    @Produces(MediaType.APPLICATION_JSON)
    public Response resolveWindow(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = id != null ? id : "";
        byte[] hexBytes = new byte[caption.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(caption.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String gauge = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + gauge});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
