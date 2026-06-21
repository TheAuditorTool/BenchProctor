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
public class BenchmarkTest03159 {

    @GET
    @Path("/BenchmarkTest03159")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest03159(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String stdinValue = java.util.Optional.ofNullable(new java.util.Scanner(System.in).nextLine()).orElse("");
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(stdinValue, "request");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        String checkedPath = "/var/app/data/" + java.nio.file.Paths.get(data).getFileName().toString();
        Files.write(Paths.get(checkedPath), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
