// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest80140 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest80140")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest80140(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = normalize(userId);
        return Response.status(500).entity(data).build();
    }
}
