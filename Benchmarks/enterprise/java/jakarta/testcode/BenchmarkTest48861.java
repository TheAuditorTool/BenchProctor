// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest48861 {

    @GET
    @Path("/BenchmarkTest48861")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest48861(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        if (request.getUserPrincipal() == null) {
            return Response.status(401).entity("not authenticated").build();
        }
        if (!"admin".equals(request.getUserPrincipal().getName())) {
            return Response.status(403).entity("forbidden").build();
        }
        return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
    }
}
