// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BenchmarkTest54592 {

    @GET
    @Path("/BenchmarkTest54592")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest54592(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String argValue = java.util.Optional.ofNullable(System.getProperty("argv.value", "")).orElse("");
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> argValue)
            .thenApply(v -> v.length() > 256 ? v.substring(0, 256).strip() : v.strip())
            .join();
        String normalizedPath = java.nio.file.Paths.get(data).normalize().toString();
        Files.delete(Paths.get("/var/app/data/" + normalizedPath));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
