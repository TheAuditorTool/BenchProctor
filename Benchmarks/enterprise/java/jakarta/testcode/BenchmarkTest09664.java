// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest09664 {

    @GET
    @Path("/BenchmarkTest09664")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09664(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(cookieValue);
        String data = wrapper.toString();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            response.sendRedirect(data);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
