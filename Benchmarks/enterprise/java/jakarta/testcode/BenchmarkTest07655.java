// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest07655 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @POST
    @Path("/BenchmarkTest07655")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest07655(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = stripCRLF(rawData);
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES/CBC/PKCS5Padding");
        javax.crypto.SecretKey key = new javax.crypto.spec.SecretKeySpec(new byte[16], "AES");
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, key, new javax.crypto.spec.IvParameterSpec(new byte[16]));
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(data.getBytes()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
