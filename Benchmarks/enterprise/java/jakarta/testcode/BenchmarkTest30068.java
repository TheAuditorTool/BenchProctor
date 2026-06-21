// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest30068 {

    @GET
    @Path("/BenchmarkTest30068")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest30068(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(envValue, "header");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        byte[] gcmIv = new byte[12]; new java.security.SecureRandom().nextBytes(gcmIv);
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES/GCM/NoPadding");
        javax.crypto.SecretKey key = new javax.crypto.spec.SecretKeySpec(new byte[16], "AES");
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, key, new javax.crypto.spec.GCMParameterSpec(128, gcmIv));
        byte[] ct = cipher.doFinal(data.getBytes());
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
