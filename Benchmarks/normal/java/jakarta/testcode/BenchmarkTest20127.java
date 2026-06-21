// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest20127 {

    @GET
    @Path("/BenchmarkTest20127")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest20127(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        response.setContentType("text/html");
        return Response.ok(hostValue, MediaType.TEXT_HTML).build();
    }
}
