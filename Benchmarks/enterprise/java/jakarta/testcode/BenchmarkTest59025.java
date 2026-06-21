// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest59025 {

    @GET
    @Path("/BenchmarkTest59025")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest59025(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : envValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        new java.io.File(data).delete();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
