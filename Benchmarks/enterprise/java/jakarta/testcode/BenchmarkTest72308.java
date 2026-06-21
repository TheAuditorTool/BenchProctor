// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest72308 {

    @GET
    @Path("/BenchmarkTest72308")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest72308(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        return Response.status(403).entity("directory listing forbidden").build();
    }
}
