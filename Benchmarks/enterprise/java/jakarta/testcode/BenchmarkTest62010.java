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
public class BenchmarkTest62010 {

    @GET
    @Path("/BenchmarkTest62010")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest62010(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String ssmValue = java.util.Optional.ofNullable(System.getenv("SSM_PARAM")).orElse("");
        String prefix = ssmValue.length() > 0 ? ssmValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = ssmValue.toLowerCase(); break;
            case "f": data = ssmValue.toUpperCase(); break;
            default: data = ssmValue.strip(); break;
        }
        byte[] keyMaterial = java.security.MessageDigest.getInstance("SHA-256").digest(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        javax.crypto.SecretKey key = new javax.crypto.spec.SecretKeySpec(java.util.Arrays.copyOf(keyMaterial, 32), "AES");
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES");
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, key);
        byte[] ct = cipher.doFinal("payload".getBytes());
        response.setHeader("X-Encrypted-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
