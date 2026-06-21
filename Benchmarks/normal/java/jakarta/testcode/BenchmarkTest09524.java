// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest09524 {

    @GET
    @Path("/BenchmarkTest09524/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09524(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = String.join(" ", pathValue.split("\\s+"));
        if ("admin".equals(data)) {
            return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
        }
        return Response.status(403).entity("forbidden").build();
    }
}
