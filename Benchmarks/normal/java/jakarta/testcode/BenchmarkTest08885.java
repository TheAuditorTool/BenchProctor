// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest08885 {

    @GET
    @Path("/BenchmarkTest08885")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest08885(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> userId)
            .thenApply(v -> v.replaceAll("[\\x00-\\x1F]", "").strip())
            .join();
        request.getSession().setMaxInactiveInterval(900);
        request.getSession().setAttribute("data", String.valueOf(data));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
