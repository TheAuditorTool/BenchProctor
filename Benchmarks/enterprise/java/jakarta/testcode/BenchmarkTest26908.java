// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest26908 {

    private static String trimEnds(String v) { return v.trim(); }

    @GET
    @Path("/BenchmarkTest26908")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest26908(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = trimEnds(authHeader);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.setHeader("X-Forwarded-For", processed);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
