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
public class BenchmarkTest52968 {

    @POST
    @Path("/BenchmarkTest52968/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest52968(@FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> commentValue)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "))
            .join();
        if (!data.matches("^[\\w\\s./\\\\:_-]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
