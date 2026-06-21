// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest61530 {

    @GET
    @Path("/BenchmarkTest61530")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest61530(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        if (!headerValue.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        return Response.ok("<div>" + headerValue + "</div>", MediaType.TEXT_HTML).build();
    }
}
