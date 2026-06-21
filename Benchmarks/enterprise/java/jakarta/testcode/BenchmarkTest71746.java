// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest71746 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest71746/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest71746(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = normalize(pathValue);
        return Response.status(500).entity(data).build();
    }
}
