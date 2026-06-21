// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest63669 {

    @GET
    @Path("/BenchmarkTest63669")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest63669(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> userId)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        if (System.currentTimeMillis() > 1000000000000L) {
            jakarta.el.ELProcessor elp = new jakarta.el.ELProcessor();
            Object rendered = elp.eval(data);
            return Response.ok("<div>" + rendered + "</div>", MediaType.TEXT_HTML).build();
        }
        return Response.ok().build();
    }
}
