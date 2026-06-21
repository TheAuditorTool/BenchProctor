// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest35389 {

    @GET
    @Path("/BenchmarkTest35389")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest35389(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        if (!forwardedIp.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        return Response.ok("<input type=\"text\" name=\"q\" value=\"" + forwardedIp + "\">", MediaType.TEXT_HTML).build();
    }
}
