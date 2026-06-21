// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest48580 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest48580/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest48580(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = normalize(pathValue);
        byte[] computed = java.security.MessageDigest.getInstance("MD5").digest(data.getBytes());
        String computedHex = java.util.Base64.getEncoder().encodeToString(computed);
        String presented = request.getHeader("X-Signature") != null ? request.getHeader("X-Signature") : "";
        if (!computedHex.equals(presented)) {
            return Response.status(403).entity("bad signature").build();
        }
        return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
    }
}
