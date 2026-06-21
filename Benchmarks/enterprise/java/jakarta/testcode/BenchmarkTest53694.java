// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest53694 {

    @GET
    @Path("/BenchmarkTest53694")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest53694(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        Integer.parseInt(envValue);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
