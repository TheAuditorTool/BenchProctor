// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest01100 {

    @GET
    @Path("/BenchmarkTest01100")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest01100(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        return Response.ok("<div>" + envValue + "</div>", MediaType.TEXT_HTML).build();
    }
}
