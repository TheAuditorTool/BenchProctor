// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest71609 {

    @GET
    @Path("/BenchmarkTest71609")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest71609(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = String.format("%s", authHeader);
        request.isUserInRole("ADMIN");
        return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
    }
}
