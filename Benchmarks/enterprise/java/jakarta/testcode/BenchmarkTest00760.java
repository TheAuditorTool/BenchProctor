// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest00760 {

    @GET
    @Path("/BenchmarkTest00760")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00760(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(authHeader);
        String data = carrier.toString();
        if (!data.isEmpty()) throw new IllegalArgumentException("invalid input: " + data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
