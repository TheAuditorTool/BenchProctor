// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest76269 {

    @GET
    @Path("/BenchmarkTest76269")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest76269(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        return Response.status(403).entity("directory listing forbidden").build();
    }
}
