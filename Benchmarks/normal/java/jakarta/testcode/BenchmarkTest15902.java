// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest15902 {

    @GET
    @Path("/BenchmarkTest15902")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest15902(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.List<String> tokens = java.util.Arrays.asList(originValue.split(","));
        String data = String.join(",", tokens);
        new java.io.File(data).delete();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
