// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest30647 {

    @GET
    @Path("/BenchmarkTest30647")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest30647(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(uaValue, "request");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        new java.io.File(data).delete();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
