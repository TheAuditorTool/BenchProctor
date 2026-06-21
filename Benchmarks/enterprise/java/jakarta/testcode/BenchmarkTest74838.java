// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest74838 {

    @GET
    @Path("/BenchmarkTest74838")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest74838(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.List<String> tokens = java.util.Arrays.asList(headerValue.split(","));
        String data = String.join(",", tokens);
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + data + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
