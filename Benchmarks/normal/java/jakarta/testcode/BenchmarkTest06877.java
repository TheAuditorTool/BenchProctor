// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest06877 {

    @GET
    @Path("/BenchmarkTest06877")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest06877(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = String.join(" ", refererValue.split("\\s+"));
        java.util.Set<String> allowed = java.util.Set.of("name", "email", "bio");
        if (!allowed.contains(data)) { return Response.status(400).build(); }
        java.util.HashMap<String,Object> entity = new java.util.HashMap<>();
        String[] kv = data.split("=", 2);
        if (kv.length == 2) {
            entity.put(kv[0], kv[1]);
            response.setHeader("X-Field-Set", kv[0]);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
