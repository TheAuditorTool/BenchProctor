// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest07191 {

    @GET
    @Path("/BenchmarkTest07191")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest07191(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(originValue, "request");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        System.loadLibrary(data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
