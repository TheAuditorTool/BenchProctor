// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest25649 {

    @GET
    @Path("/BenchmarkTest25649")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest25649(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(headerValue, "json");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        return Response.status(500).entity(data).build();
    }
}
