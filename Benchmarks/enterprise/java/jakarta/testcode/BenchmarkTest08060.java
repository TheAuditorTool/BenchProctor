// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest08060 {

    @GET
    @Path("/BenchmarkTest08060")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest08060(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Function<String, String> tabNormalizer = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::strip);
        String data = decorated.apply(userId);
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + data}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
