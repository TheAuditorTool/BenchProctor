// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest50529 {

    @GET
    @Path("/BenchmarkTest50529")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest50529(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Function<String, String> initialFn = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::trim);
        String data = transformed.apply(userId);
        response.setContentType("text/html");
        return Response.ok(data, MediaType.TEXT_HTML).build();
    }
}
