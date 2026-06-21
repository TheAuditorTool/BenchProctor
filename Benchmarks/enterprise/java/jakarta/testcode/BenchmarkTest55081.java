// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest55081 {

    @GET
    @Path("/BenchmarkTest55081")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest55081(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        try {
            Integer.parseInt(headerValue);
        } catch (Exception ignored) {
        }
        return Response.ok("{\"status\":\"ok\"}", MediaType.APPLICATION_JSON).build();
    }
}
