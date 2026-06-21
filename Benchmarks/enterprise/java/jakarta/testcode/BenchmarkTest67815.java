// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BenchmarkTest67815 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @POST
    @Path("/BenchmarkTest67815")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest67815(@Valid UserInput req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        java.util.function.Function<String, String> tabNormalizer = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::strip);
        String data = decorated.apply(jsonValue);
        String normalizedPath = java.nio.file.Paths.get(data).normalize().toString();
        Files.delete(Paths.get("/var/app/data/" + normalizedPath));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
