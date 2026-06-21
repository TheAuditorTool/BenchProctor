// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest19031 {

    @GET
    @Path("/BenchmarkTest19031")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest19031(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        response.setContentType("text/html");
        return Response.ok(forwardedIp, MediaType.TEXT_HTML).build();
    }
}
