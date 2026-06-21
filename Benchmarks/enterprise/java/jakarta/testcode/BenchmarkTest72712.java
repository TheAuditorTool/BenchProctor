// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest72712 {

    private static String trimEnds(String v) { return v.trim(); }

    @GET
    @Path("/BenchmarkTest72712")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest72712(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = trimEnds(userId);
        return Response.status(500).entity(data).build();
    }
}
