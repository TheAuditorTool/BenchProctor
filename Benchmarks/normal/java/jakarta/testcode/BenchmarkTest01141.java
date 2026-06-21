// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest01141 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest01141")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest01141(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = stripWhitespace(authHeader);
        int requested = Integer.parseInt(data);
        int allocSize = requested + 1;
        response.setHeader("X-Alloc-Size", String.valueOf(allocSize));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
