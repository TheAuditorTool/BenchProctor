// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest62491 {

    @GET
    @Path("/BenchmarkTest62491")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest62491(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.function.Function<String, String> preprocessor = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> fullPipeline = preprocessor.andThen(String::strip);
        String data = fullPipeline.apply(cookieValue);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            response.getWriter().print("<div>" + data + "</div>");
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        return Response.ok().build();
    }
}
