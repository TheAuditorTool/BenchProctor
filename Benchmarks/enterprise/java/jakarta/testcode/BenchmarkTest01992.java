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
public class BenchmarkTest01992 {

    @GET
    @Path("/BenchmarkTest01992/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest01992(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> pathValue)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "))
            .join();
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            String content = Files.readString(Paths.get("/var/app/data/" + data), java.nio.charset.StandardCharsets.UTF_8);
            response.setHeader("X-File-Bytes", String.valueOf(content.length()));
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
