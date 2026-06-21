// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest21236 {

    @GET
    @Path("/BenchmarkTest21236")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest21236(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        Integer.parseInt(userId);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
