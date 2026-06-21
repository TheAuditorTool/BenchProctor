// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest01529 {

    @GET
    @Path("/BenchmarkTest01529")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest01529(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(hostValue, "json");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
