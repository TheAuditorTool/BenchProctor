// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest58986 {

    @GET
    @Path("/BenchmarkTest58986")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest58986(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        if (!userId.isEmpty()) throw new Exception("processing error: " + userId);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
