// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest06039 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @GET
    @Path("/BenchmarkTest06039/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest06039(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = collapseWhitespace(pathValue);
        if ("admin".equals(data) || "ROLE_ADMIN".equals(data)) {
            return Response.ok("{\"status\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
        return Response.status(403).entity("forbidden").build();
    }
}
