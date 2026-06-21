// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest68412 {

    @GET
    @Path("/BenchmarkTest68412/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest68412(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = java.net.URLDecoder.decode(pathValue, "UTF-8");
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
