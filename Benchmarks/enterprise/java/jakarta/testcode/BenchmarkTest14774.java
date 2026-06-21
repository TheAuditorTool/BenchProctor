// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest14774 {

    @GET
    @Path("/BenchmarkTest14774")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest14774(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        return Response.ok("<div>" + headerValue + "</div>", MediaType.TEXT_HTML).build();
    }
}
