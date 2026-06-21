// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest73788 {

    @GET
    @Path("/BenchmarkTest73788")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest73788(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        if (request.getUserPrincipal() == null) {
            return Response.status(401).entity("not authenticated").build();
        }
        if (request.getSession().getAttribute("user") == null) { return Response.status(401).build(); }
        return Response.status(500).entity("Internal error").build();
    }
}
