// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest27455 {

    @GET
    @Path("/BenchmarkTest27455")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest27455(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(userId);
        String data = carrier.toString();
        if (!data.matches("^[\\w\\s.,;:_/\\-=]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        int requested = Integer.parseInt(data);
        int allocSize = requested + 1;
        response.setHeader("X-Alloc-Size", String.valueOf(allocSize));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
