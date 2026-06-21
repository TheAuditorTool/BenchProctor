// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest41813 {

    @GET
    @Path("/BenchmarkTest41813")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest41813(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(cookieValue, "cookie");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        int result = 100 / Integer.parseInt(data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
