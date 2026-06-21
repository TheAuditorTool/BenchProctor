// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest64946 {

    @GET
    @Path("/BenchmarkTest64946")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest64946(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.List<String> tokens = java.util.Arrays.asList(authHeader.split(","));
        String data = String.join(",", tokens);
        response.sendRedirect(data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
