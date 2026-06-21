// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest12169 {

    @GET
    @Path("/BenchmarkTest12169")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12169(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String data = envValue.isEmpty() ? "default" : envValue;
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
