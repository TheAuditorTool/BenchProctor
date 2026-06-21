// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest13822 {

    @GET
    @Path("/BenchmarkTest13822")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest13822(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> authHeader)
            .thenApply(v -> v.length() > 256 ? v.substring(0, 256).strip() : v.strip())
            .join();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + processed}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
