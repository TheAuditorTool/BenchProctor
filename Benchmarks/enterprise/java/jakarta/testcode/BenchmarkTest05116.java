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
public class BenchmarkTest05116 {

    @GET
    @Path("/BenchmarkTest05116")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest05116(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Function<String, String> preprocessor = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> fullPipeline = preprocessor.andThen(String::strip);
        String data = fullPipeline.apply(userId);
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
