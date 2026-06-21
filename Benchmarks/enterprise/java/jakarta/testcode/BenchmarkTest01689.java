// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest01689 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest01689")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest01689(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String data = normalize(envValue);
        Integer.parseInt(data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
