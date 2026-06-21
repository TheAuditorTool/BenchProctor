// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest26287 {

    @GET
    @Path("/BenchmarkTest26287")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest26287(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        response.setHeader("Access-Control-Allow-Origin", authHeader);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
