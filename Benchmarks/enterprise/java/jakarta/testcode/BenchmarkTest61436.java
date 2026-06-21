// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest61436 {

    @GET
    @Path("/BenchmarkTest61436")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest61436(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> refererValue)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        int divisor = Integer.parseInt(data);
        if (divisor == 0) { return Response.status(400).build(); }
        int result = 100 / divisor;
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
