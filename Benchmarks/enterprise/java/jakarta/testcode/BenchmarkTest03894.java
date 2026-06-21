// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest03894 {

    @GET
    @Path("/BenchmarkTest03894/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest03894(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        if (request.getUserPrincipal() == null) {
            return Response.status(401).entity("not authenticated").build();
        }
        if ("admin".equals(pathValue) || "ROLE_ADMIN".equals(pathValue)) {
            return Response.ok("{\"status\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
        return Response.status(403).entity("forbidden").build();
    }
}
