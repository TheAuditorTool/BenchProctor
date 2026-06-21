// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest79018 {

    @GET
    @Path("/BenchmarkTest79018/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest79018(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(pathValue, "form");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        response.setHeader("Access-Control-Allow-Origin", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
