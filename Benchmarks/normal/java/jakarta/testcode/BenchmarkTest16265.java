// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16265 {

    @GET
    @Path("/BenchmarkTest16265")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16265(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("\\s+", " ");
        String data = transform.apply(userId);
        response.setHeader("X-Forwarded-For", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
