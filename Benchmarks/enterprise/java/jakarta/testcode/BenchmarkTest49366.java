// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest49366 {

    @GET
    @Path("/BenchmarkTest49366/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest49366(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(pathValue, "body");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        return Response.ok("{\"resource\":\"" + data + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
