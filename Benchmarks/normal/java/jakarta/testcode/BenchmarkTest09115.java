// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest09115 {

    @GET
    @Path("/BenchmarkTest09115/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09115(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = "[%s]".formatted(pathValue);
        javax.crypto.Mac authMac = javax.crypto.Mac.getInstance("HmacSHA256");
        authMac.init(new javax.crypto.spec.SecretKeySpec(System.getenv("HMAC_SECRET").getBytes(java.nio.charset.StandardCharsets.UTF_8), "HmacSHA256"));
        byte[] presented = authMac.doFinal(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        byte[] stored = java.util.Base64.getDecoder().decode((String) request.getSession().getAttribute("credHash"));
        if (!java.security.MessageDigest.isEqual(presented, stored)) { return Response.status(401).build(); }
        return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
    }
}
