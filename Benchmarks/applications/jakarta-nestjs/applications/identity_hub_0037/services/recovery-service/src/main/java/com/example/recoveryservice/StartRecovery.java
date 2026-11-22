// SPDX-License-Identifier: Apache-2.0
package com.example.recoveryservice;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.annotation.security.RolesAllowed;

@Path("/")
public class StartRecovery {

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/StartRecovery/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    @RolesAllowed("USER")
    public Response startRecovery(@javax.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String remark = pathId;
        valueRef.set(remark);
        String persona = valueRef.get();
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://consent-registry:3000/consent-registry/recordConsent").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"identity_payload\": \"" + persona + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
