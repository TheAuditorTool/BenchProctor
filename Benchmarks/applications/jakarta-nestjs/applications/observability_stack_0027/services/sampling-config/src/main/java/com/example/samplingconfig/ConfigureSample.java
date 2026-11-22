// SPDX-License-Identifier: Apache-2.0
package com.example.samplingconfig;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class ConfigureSample {


    @GET
    @Path("/ConfigureSample/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response configureSample(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = pathId;
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("[ \\t]+", " ");
        lengthGuard.accept(remark);
        String gauge = normalizer.apply(remark);
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://retention-service:3000/retention-service/sweepRetention").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"telemetry_payload\": \"" + gauge + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
