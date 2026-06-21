// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest07495 {

    @GET
    @Path("/BenchmarkTest07495")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest07495(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(headerValue, "request");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        new java.io.File(data).delete();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
