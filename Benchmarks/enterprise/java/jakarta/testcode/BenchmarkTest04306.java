// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest04306 {

    @GET
    @Path("/BenchmarkTest04306")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest04306(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        StringBuilder payload = new StringBuilder();
        payload.append(envValue);
        String data = payload.toString();
        return Response.status(500).entity(data).build();
    }
}
