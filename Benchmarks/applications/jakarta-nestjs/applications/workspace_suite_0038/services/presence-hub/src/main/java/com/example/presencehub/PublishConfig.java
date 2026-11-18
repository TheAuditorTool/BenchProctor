// SPDX-License-Identifier: Apache-2.0
package com.example.presencehub;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class PublishConfig {


    @GET
    @Path("/PublishConfig")
    @Produces(MediaType.APPLICATION_JSON)
    public Response publishConfig(@jakarta.validation.constraints.Size(max = 4096) @QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String preface = id != null ? id : "";
        byte[] hexBytes = new byte[preface.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(preface.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String remark = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(remark)) { return Response.status(403).build(); }
        String wording = remark;
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + wording}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
