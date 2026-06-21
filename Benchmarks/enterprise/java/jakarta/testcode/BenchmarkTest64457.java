// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest64457 {

    @GET
    @Path("/BenchmarkTest64457")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest64457(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String prefix = forwardedIp.length() > 0 ? forwardedIp.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = forwardedIp.toLowerCase(); break;
            case "f": data = forwardedIp.toUpperCase(); break;
            default: data = forwardedIp.strip(); break;
        }
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("DES/ECB/PKCS5Padding");
        javax.crypto.SecretKey key = new javax.crypto.spec.SecretKeySpec(new byte[8], "DES");
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, key);
        byte[] ct = cipher.doFinal(data.getBytes());
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
