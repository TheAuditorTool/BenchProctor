// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest08967 {

    @GET
    @Path("/BenchmarkTest08967")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest08967(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        if (!String.valueOf(userId).equals(request.getSession().getAttribute("csrfToken"))) {
            return Response.status(403).entity("csrf mismatch").build();
        }
        String sessionRole = String.valueOf(request.getSession().getAttribute("role"));
        if (!"admin".equals(sessionRole)) { return Response.status(403).entity("forbidden").build(); }
        response.setContentType("application/json");
        return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
    }
}
