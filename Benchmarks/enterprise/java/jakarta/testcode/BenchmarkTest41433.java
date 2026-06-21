// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest41433 {

    @GET
    @Path("/BenchmarkTest41433")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest41433(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        StringBuilder envelope = new StringBuilder();
        envelope.append(envValue);
        String data = envelope.toString();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            System.loadLibrary(data);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
