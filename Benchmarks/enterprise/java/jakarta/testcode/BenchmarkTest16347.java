// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16347 {

    @GET
    @Path("/BenchmarkTest16347")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16347(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        byte[] computed = java.security.MessageDigest.getInstance("MD5").digest(userId.getBytes());
        String computedHex = java.util.Base64.getEncoder().encodeToString(computed);
        String presented = request.getHeader("X-Signature") != null ? request.getHeader("X-Signature") : "";
        if (!computedHex.equals(presented)) {
            return Response.status(403).entity("bad signature").build();
        }
        return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
    }
}
