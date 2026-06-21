// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest42011 {

    @GET
    @Path("/BenchmarkTest42011")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest42011(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String argValue = java.util.Optional.ofNullable(System.getProperty("argv.value", "")).orElse("");
        StringBuilder payload = new StringBuilder();
        payload.append(argValue);
        String data = payload.toString();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + data}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
