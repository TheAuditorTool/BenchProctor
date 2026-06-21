// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.security.*;

@Path("/")
public class BenchmarkTest23470 {

    @GET
    @Path("/BenchmarkTest23470")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest23470(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(originValue, "body");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        byte[] hashSalt = new byte[16]; new java.security.SecureRandom().nextBytes(hashSalt);
        java.security.MessageDigest hashMd = java.security.MessageDigest.getInstance("SHA-256");
        hashMd.update(hashSalt);
        byte[] digest = hashMd.digest(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
