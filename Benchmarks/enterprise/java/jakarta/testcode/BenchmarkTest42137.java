// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest42137 {

    @GET
    @Path("/BenchmarkTest42137")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest42137(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(envValue, "json");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        if (!data.isEmpty()) throw new IllegalArgumentException("invalid input: " + data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
