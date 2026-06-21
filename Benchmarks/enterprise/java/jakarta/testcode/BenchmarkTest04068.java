// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest04068 {

    @GET
    @Path("/BenchmarkTest04068")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest04068(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        return Response.status(403).entity("directory listing forbidden").build();
    }
}
