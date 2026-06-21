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
public class BenchmarkTest78648 {

    @GET
    @Path("/BenchmarkTest78648")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest78648(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uploadedName = java.util.Optional.ofNullable((String) request.getAttribute("uploadName")).orElse("");
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(uploadedName, "http");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        String checkedPath = "/var/app/data/" + java.nio.file.Paths.get(data).getFileName().toString();
        Files.delete(Paths.get(checkedPath));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
