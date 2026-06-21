// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.security.*;

@Path("/")
public class BenchmarkTest19761 {

    @POST
    @Path("/BenchmarkTest19761")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest19761(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = String.format("%s", fieldValue);
        byte[] hashSalt = new byte[16]; new java.security.SecureRandom().nextBytes(hashSalt);
        java.security.MessageDigest hashMd = java.security.MessageDigest.getInstance("SHA-256");
        hashMd.update(hashSalt);
        byte[] digest = hashMd.digest(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
