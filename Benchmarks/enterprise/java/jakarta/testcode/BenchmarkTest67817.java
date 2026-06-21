// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest67817 {

    @POST
    @Path("/BenchmarkTest67817")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest67817(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        return Response.status(500).entity("Internal error").build();
    }
}
