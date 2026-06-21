// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest18635 {

    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest18635")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18635(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        holder.set(envValue);
        String data = holder.get();
        String trustedClaim = data;
        response.setHeader("X-Claim-Trusted", trustedClaim);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
