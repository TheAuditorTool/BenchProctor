// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest00631 {

    @GET
    @Path("/BenchmarkTest00631")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00631(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        StringBuilder payload = new StringBuilder();
        payload.append(authHeader);
        String data = payload.toString();
        return Response.status(500).entity(data).build();
    }
}
