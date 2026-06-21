// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.util.Random;

@Path("/")
public class BenchmarkTest62212 {

    @GET
    @Path("/BenchmarkTest62212")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest62212(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        byte[] tokenBytes = new byte[32];
        new java.security.SecureRandom().nextBytes(tokenBytes);
        String randToken = java.util.HexFormat.of().formatHex(tokenBytes);
        response.setHeader("X-Rand", randToken);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
