// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest23163 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest23163")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest23163(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String data = normalize(envValue);
        return Response.status(500).entity(data).build();
    }
}
