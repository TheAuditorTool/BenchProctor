// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest76155 {

    @GET
    @Path("/BenchmarkTest76155")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest76155(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        response.addCookie(new Cookie("session", headerValue));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
