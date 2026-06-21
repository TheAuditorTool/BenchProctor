// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.security.*;

@Path("/")
public class BenchmarkTest12852 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @GET
    @Path("/BenchmarkTest12852")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12852(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = toLowerCase(refererValue);
        byte[] passwordSalt = new byte[16]; new java.security.SecureRandom().nextBytes(passwordSalt);
        javax.crypto.SecretKeyFactory skf = javax.crypto.SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        byte[] derived = skf.generateSecret(new javax.crypto.spec.PBEKeySpec(data.toCharArray(), passwordSalt, 100000, 256)).getEncoded();
        response.setHeader("X-PBKDF2", java.util.Base64.getEncoder().encodeToString(derived));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
