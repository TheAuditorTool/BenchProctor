// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest26091 {

    @GET
    @Path("/BenchmarkTest26091")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest26091(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        response.addCookie(new Cookie("session", forwardedIp));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
