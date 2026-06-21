// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest26385 {

    @GET
    @Path("/BenchmarkTest26385")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest26385(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Function<String, String> tabNormalizer = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::trim);
        String data = decorated.apply(userId);
        if (!data.matches("^[\\w\\s.,;:_/\\-=]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        return Response.status(500).entity(data).build();
    }
}
