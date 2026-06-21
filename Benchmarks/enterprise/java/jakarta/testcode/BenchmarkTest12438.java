// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest12438 {

    @GET
    @Path("/BenchmarkTest12438")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12438(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String data;
        try { data = String.valueOf(Integer.parseInt(envValue)); }
        catch (NumberFormatException e) { data = envValue; }
        int requested = Integer.parseInt(data);
        int allocSize = requested + 1;
        response.setHeader("X-Alloc-Size", String.valueOf(allocSize));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
