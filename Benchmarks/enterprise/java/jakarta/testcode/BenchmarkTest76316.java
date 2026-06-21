// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest76316 {

    @GET
    @Path("/BenchmarkTest76316")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest76316(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        StringBuilder payload = new StringBuilder();
        payload.append(userId);
        String data = payload.toString();
        if ("admin".equals(data) || "ROLE_ADMIN".equals(data)) {
            return Response.ok("{\"status\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
        return Response.status(403).entity("forbidden").build();
    }
}
