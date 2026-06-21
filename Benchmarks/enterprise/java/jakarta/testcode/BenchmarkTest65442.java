// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest65442 {

    @GET
    @Path("/BenchmarkTest65442")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest65442(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        if (!userId.isEmpty()) throw new IllegalArgumentException("invalid input: " + userId);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
