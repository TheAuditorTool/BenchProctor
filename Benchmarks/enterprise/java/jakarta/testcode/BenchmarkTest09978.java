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
public class BenchmarkTest09978 {

    @GET
    @Path("/BenchmarkTest09978")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09978(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uploadedName = java.util.Optional.ofNullable((String) request.getAttribute("uploadName")).orElse("");
        String data;
        if (uploadedName.length() > 256) { data = uploadedName.substring(0, 256); }
        else { data = uploadedName; }
        Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
