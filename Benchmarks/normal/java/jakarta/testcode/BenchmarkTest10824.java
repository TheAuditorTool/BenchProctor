// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest10824 {

    @POST
    @Path("/BenchmarkTest10824")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest10824(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(fieldValue, "http");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + data + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
