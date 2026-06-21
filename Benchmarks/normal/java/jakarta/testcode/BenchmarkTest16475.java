// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16475 {

    @GET
    @Path("/BenchmarkTest16475")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16475(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(uaValue, "query");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        return Response.status(500).entity(data).build();
    }
}
