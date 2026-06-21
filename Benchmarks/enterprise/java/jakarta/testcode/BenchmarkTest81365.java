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
public class BenchmarkTest81365 {

    @GET
    @Path("/BenchmarkTest81365/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest81365(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Function<String, String> tabNormalizer = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::trim);
        String data = decorated.apply(pathValue);
        String normalizedPath = java.nio.file.Paths.get(data).normalize().toString();
        Files.delete(Paths.get("/var/app/data/" + normalizedPath));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
