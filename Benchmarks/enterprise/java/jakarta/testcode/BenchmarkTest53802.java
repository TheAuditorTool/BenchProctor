// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

@Path("/")
public class BenchmarkTest53802 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @GET
    @Path("/BenchmarkTest53802")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest53802(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String ssmValue = java.util.Optional.ofNullable(System.getenv("SSM_PARAM")).orElse("");
        String data = toLowerCase(ssmValue);
        byte[] kdfMaterial = java.security.MessageDigest.getInstance("SHA-256").digest(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        javax.crypto.SecretKey key = new javax.crypto.spec.SecretKeySpec(java.util.Arrays.copyOf(kdfMaterial, 32), "AES");
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES/GCM/NoPadding");
        byte[] gcmIv = new byte[12]; new java.security.SecureRandom().nextBytes(gcmIv);
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, key, new javax.crypto.spec.GCMParameterSpec(128, gcmIv));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
