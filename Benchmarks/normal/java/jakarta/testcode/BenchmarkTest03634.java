// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest03634 {

    @GET
    @Path("/BenchmarkTest03634")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest03634(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + forwardedIp;
        String data = valueSupplier.get();
        String forwardedFor = request.getHeader("X-Forwarded-For");
        String clientIp = forwardedFor != null ? forwardedFor : data;
        if ("127.0.0.1".equals(clientIp) || "10.0.0.1".equals(clientIp)) {
            return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
        }
        return Response.status(403).entity("forbidden").build();
    }
}
