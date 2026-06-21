// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest55507 {

    @GET
    @Path("/BenchmarkTest55507/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest55507(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.List<String> tokens = java.util.Arrays.asList(pathValue.split(","));
        String data = String.join(",", tokens);
        request.isUserInRole("ADMIN");
        return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
    }
}
