// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest73647 {

    @GET
    @Path("/BenchmarkTest73647")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest73647(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        if (request.getUserPrincipal() == null) {
            return Response.status(401).entity("not authenticated").build();
        }
        if ("admin".equals(uaValue) || "ROLE_ADMIN".equals(uaValue)) {
            return Response.ok("{\"status\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
        return Response.status(403).entity("forbidden").build();
    }
}
