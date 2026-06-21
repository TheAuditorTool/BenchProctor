// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest18884 {

    @GET
    @Path("/BenchmarkTest18884")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18884(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + cookieValue;
        String data = valueSupplier.get();
        java.security.KeyPairGenerator kpg = java.security.KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048);
        java.security.KeyPair kp = kpg.generateKeyPair();
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("RSA/ECB/PKCS1Padding");
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, kp.getPublic());
        byte[] ptBytes = data.getBytes(java.nio.charset.StandardCharsets.UTF_8);
        byte[] ptSlice = java.util.Arrays.copyOf(ptBytes, Math.min(ptBytes.length, 190));
        byte[] ct = cipher.doFinal(ptSlice);
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
