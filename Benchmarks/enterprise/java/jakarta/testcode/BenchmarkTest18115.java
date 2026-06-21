// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest18115 {

    @GET
    @Path("/BenchmarkTest18115")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18115(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(refererValue, "query");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        if (!data.isEmpty()) throw new IllegalArgumentException("invalid input: " + data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
