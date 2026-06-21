// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest78896 {

    @GET
    @Path("/BenchmarkTest78896")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest78896(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.Properties container = new java.util.Properties();
        container.load(new java.io.StringReader("rawValue=" + originValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", container.getProperty("format", "plain"));
        String data = container.getProperty("rawValue", "");
        byte[] computed = java.security.MessageDigest.getInstance("MD5").digest(data.getBytes());
        String computedHex = java.util.Base64.getEncoder().encodeToString(computed);
        String presented = request.getHeader("X-Signature") != null ? request.getHeader("X-Signature") : "";
        if (!computedHex.equals(presented)) {
            return Response.status(403).entity("bad signature").build();
        }
        return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
    }
}
