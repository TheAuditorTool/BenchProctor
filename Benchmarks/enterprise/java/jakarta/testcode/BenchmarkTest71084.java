// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest71084 {

    @GET
    @Path("/BenchmarkTest71084")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest71084(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(originValue, "header");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        return Response.ok(data + ",data\n", "text/csv").build();
    }
}
