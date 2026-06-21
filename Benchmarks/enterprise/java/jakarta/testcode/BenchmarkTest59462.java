// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest59462 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest59462/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest59462(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = normalize(pathValue);
        return Response.status(500).entity(data).build();
    }
}
