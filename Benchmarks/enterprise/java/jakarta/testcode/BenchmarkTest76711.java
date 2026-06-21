// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest76711 {

    @GET
    @Path("/BenchmarkTest76711")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest76711(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        return Response.ok("<div>" + envValue + "</div>", MediaType.TEXT_HTML).build();
    }
}
