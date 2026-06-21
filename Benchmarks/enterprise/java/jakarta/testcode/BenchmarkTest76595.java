// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest76595 {

    @GET
    @Path("/BenchmarkTest76595/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest76595(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = pathValue.replace("\u0000", "");
        return Response.status(500).entity(data).build();
    }
}
