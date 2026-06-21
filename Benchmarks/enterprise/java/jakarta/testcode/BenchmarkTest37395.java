// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest37395 {

    @GET
    @Path("/BenchmarkTest37395")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest37395(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String apiBody = java.util.Optional.ofNullable(new java.io.BufferedReader(new java.io.InputStreamReader(new java.net.URL("https://api.svc.local/data").openStream())).readLine()).orElse("");
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> apiBody)
            .thenApply(v -> v.replace("\t", " ").strip())
            .join();
        java.net.URI parsed = java.net.URI.create(data);
        String parsedHost = parsed.getHost() == null ? "" : parsed.getHost();
        if (!parsedHost.endsWith(".svc.local") && !parsedHost.endsWith(".acmecdn.net")) {
            return Response.status(403).entity("forbidden host").build();
        }
        String targetUrl = data;
        response.sendRedirect(targetUrl);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
