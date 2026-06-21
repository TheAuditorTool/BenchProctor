// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest39062 {

    @GET
    @Path("/BenchmarkTest39062")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest39062(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        response.setContentType("text/html");
        return Response.ok(cookieValue, MediaType.TEXT_HTML).build();
    }
}
