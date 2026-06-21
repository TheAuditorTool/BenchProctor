// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest11825 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest11825")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest11825(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = normalize(authHeader);
        if (!String.valueOf(data).equals(request.getSession().getAttribute("csrfToken"))) {
            return Response.status(403).entity("csrf mismatch").build();
        }
        String sessionRole = String.valueOf(request.getSession().getAttribute("role"));
        if (!"admin".equals(sessionRole)) { return Response.status(403).entity("forbidden").build(); }
        response.setContentType("application/json");
        return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
    }
}
