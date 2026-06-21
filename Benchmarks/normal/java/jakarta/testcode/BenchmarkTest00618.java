// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest00618 {

    @GET
    @Path("/BenchmarkTest00618")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00618(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(userId, "form");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        response.setContentType("text/html");
        return Response.ok(data, MediaType.TEXT_HTML).build();
    }
}
