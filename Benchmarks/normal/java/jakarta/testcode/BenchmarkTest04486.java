// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest04486 {

    @GET
    @Path("/BenchmarkTest04486")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest04486(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(cookieValue, "body");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        return Response.status(500).entity(data).build();
    }
}
