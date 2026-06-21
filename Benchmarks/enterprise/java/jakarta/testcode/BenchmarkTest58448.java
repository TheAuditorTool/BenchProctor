// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest58448 {

    @GET
    @Path("/BenchmarkTest58448")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest58448(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        response.sendRedirect(headerValue);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
