// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest78933 {

    @POST
    @Path("/BenchmarkTest78933")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest78933(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(rawData, "cookie");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        try {
            Integer.parseInt(data);
        } catch (Exception ignored) {
        }
        return Response.ok("{\"status\":\"ok\"}", MediaType.APPLICATION_JSON).build();
    }
}
