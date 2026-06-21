// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest29089 {

    @GET
    @Path("/BenchmarkTest29089")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest29089(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        request.getSession().setAttribute("data", String.valueOf(authHeader));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
