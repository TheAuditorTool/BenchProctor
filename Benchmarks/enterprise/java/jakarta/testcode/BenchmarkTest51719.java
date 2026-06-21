// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest51719 {

    @GET
    @Path("/BenchmarkTest51719")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest51719(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(userId, "request");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        return Response.status(500).entity(data).build();
    }
}
