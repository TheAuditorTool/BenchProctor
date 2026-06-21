// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest11132 {

    @GET
    @Path("/BenchmarkTest11132")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest11132(@CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.function.Function<String, String> firstStage = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::strip);
        String data = composed.apply(cookieValue);
        if (System.currentTimeMillis() > 1000000000000L) {
            Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + data}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
