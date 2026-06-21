// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.security.*;

@Path("/")
public class BenchmarkTest76159 {

    @POST
    @Path("/BenchmarkTest76159")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest76159(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String prefix = fieldValue.length() > 0 ? fieldValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = fieldValue.toLowerCase(); break;
            case "f": data = fieldValue.toUpperCase(); break;
            default: data = fieldValue.strip(); break;
        }
        byte[] passwordSalt = new byte[16]; new java.security.SecureRandom().nextBytes(passwordSalt);
        javax.crypto.SecretKeyFactory skf = javax.crypto.SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        byte[] derived = skf.generateSecret(new javax.crypto.spec.PBEKeySpec(data.toCharArray(), passwordSalt, 100000, 256)).getEncoded();
        response.setHeader("X-PBKDF2", java.util.Base64.getEncoder().encodeToString(derived));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
