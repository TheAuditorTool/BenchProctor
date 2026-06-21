// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest22282 {

    @GET
    @Path("/BenchmarkTest22282")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest22282(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        if (!cookieValue.matches("^[a-zA-Z0-9_.-]+$")) { return Response.status(400).build(); }
        String normalized = java.text.Normalizer.normalize(cookieValue, java.text.Normalizer.Form.NFKC);
        response.setContentType("text/html");
        return Response.ok("<p>" + normalized + "</p>", MediaType.TEXT_HTML).build();
    }
}
