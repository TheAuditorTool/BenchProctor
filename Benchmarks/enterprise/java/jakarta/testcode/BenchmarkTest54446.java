// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest54446 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest54446")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest54446(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = normalize(authHeader);
        if (!("true".equals(data) || "false".equals(data))) { return Response.status(400).build(); }
        String trustedClaim = data;
        response.setHeader("X-Claim-Trusted", trustedClaim);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
