// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest00639 {

    @GET
    @Path("/BenchmarkTest00639/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00639(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        if (!pathValue.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        response.setHeader("Refresh", "0; url=" + pathValue);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
