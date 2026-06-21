// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest00986 {

    @POST
    @Path("/BenchmarkTest00986")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00986(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        byte[] raw = xmlValue.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String data = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES/CBC/PKCS5Padding");
        javax.crypto.SecretKey key = new javax.crypto.spec.SecretKeySpec(new byte[16], "AES");
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, key, new javax.crypto.spec.IvParameterSpec(new byte[16]));
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(data.getBytes()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
