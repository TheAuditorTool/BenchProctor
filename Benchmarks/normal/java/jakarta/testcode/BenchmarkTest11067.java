// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest11067 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest11067")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest11067(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = normalize(forwardedIp);
        String forwardedFor = request.getHeader("X-Forwarded-For");
        String clientIp = forwardedFor != null ? forwardedFor : data;
        if ("127.0.0.1".equals(clientIp) || "10.0.0.1".equals(clientIp)) {
            return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
        }
        return Response.status(403).entity("forbidden").build();
    }
}
