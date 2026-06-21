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
public class BenchmarkTest15019 {

    @GET
    @Path("/BenchmarkTest15019/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest15019(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Function<String, String> initialFn = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::strip);
        String data = transformed.apply(pathValue);
        String normalizedPath = java.nio.file.Paths.get(data).normalize().toString();
        Files.delete(Paths.get("/var/app/data/" + normalizedPath));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
