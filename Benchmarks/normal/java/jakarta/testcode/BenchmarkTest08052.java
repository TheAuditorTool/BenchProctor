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
public class BenchmarkTest08052 {

    @GET
    @Path("/BenchmarkTest08052")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest08052(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uploadedName = java.util.Optional.ofNullable((String) request.getAttribute("uploadName")).orElse("");
        Files.delete(Paths.get("/var/app/data/" + uploadedName));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
