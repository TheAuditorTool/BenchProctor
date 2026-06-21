// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest42597 {

    @GET
    @Path("/BenchmarkTest42597")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest42597(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> userId)
            .thenApply(v -> v.replace("\t", " ").strip())
            .join();
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
