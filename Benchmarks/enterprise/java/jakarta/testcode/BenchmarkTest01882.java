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
public class BenchmarkTest01882 {

    @GET
    @Path("/BenchmarkTest01882")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest01882(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uploadedName = java.util.Optional.ofNullable((String) request.getAttribute("uploadName")).orElse("");
        java.util.function.Function<String, String> firstStage = s -> s.replace("\r", "").replace("\n", "");
        java.util.function.Function<String, String> composed = firstStage.andThen(String::strip);
        String data = composed.apply(uploadedName);
        if (!data.endsWith(".jpg") && !data.endsWith(".png")) { return Response.status(400).build(); }
        String entryFile = data;
        Files.write(Paths.get("/var/uploads/" + entryFile), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
