// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest11618 {

    @GET
    @Path("/BenchmarkTest11618")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest11618(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String prefix = userId.length() > 0 ? userId.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = userId.toLowerCase(); break;
            case "f": data = userId.toUpperCase(); break;
            default: data = userId.strip(); break;
        }
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
