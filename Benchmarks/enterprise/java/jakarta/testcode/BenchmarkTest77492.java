// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest77492 {

    @GET
    @Path("/BenchmarkTest77492")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest77492(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(originValue, "header");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        return Response.status(500).entity(data).build();
    }
}
