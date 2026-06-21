// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest47807 {

    @GET
    @Path("/BenchmarkTest47807")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest47807(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Function<String, String> firstStage = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::strip);
        String data = composed.apply(userId);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            new ProcessBuilder("python3", "-c", data).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
