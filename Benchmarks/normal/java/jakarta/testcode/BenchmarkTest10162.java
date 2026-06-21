// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest10162 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest10162")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest10162(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = normalize(authHeader);
        return Response.status(500).entity(data).build();
    }
}
