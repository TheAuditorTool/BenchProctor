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
public class BenchmarkTest05057 {

    @GET
    @Path("/BenchmarkTest05057")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest05057(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uploadedName = java.util.Optional.ofNullable((String) request.getAttribute("uploadName")).orElse("");
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(uploadedName.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String data = String.join(",", lowered);
        Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
