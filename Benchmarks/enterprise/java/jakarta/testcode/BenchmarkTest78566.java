// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest78566 {

    @GET
    @Path("/BenchmarkTest78566/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest78566(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        return Response.status(500).entity(pathValue).build();
    }
}
