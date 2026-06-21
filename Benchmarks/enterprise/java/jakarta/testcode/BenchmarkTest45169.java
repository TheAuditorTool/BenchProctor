// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.security.*;

@Path("/")
public class BenchmarkTest45169 {

    @GET
    @Path("/BenchmarkTest45169")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest45169(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(uaValue);
        String data = normalizer.apply(uaValue);
        byte[] passwordSalt = new byte[16]; new java.security.SecureRandom().nextBytes(passwordSalt);
        javax.crypto.SecretKeyFactory skf = javax.crypto.SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        byte[] derived = skf.generateSecret(new javax.crypto.spec.PBEKeySpec(data.toCharArray(), passwordSalt, 100000, 256)).getEncoded();
        response.setHeader("X-PBKDF2", java.util.Base64.getEncoder().encodeToString(derived));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
