// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest60654 {

    @GET
    @Path("/BenchmarkTest60654")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest60654(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String apiBody = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(new java.net.URL("https://api.svc.local/data").openStream())).readLine()).orElse("");
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> apiBody)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "))
            .join();
        if (data.length() > 2048) { return Response.status(400).entity("schema invalid").build(); }
        response.sendRedirect(data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
