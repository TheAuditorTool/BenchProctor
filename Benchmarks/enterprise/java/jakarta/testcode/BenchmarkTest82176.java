// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest82176 {

    @GET
    @Path("/BenchmarkTest82176")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest82176(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(cookieValue, "http");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        request.getSession().setAttribute("data", String.valueOf(data));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
