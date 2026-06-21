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
public class BenchmarkTest66462 {

    @GET
    @Path("/BenchmarkTest66462/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest66462(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        if (!pathValue.endsWith(".jpg") && !pathValue.endsWith(".png")) { return Response.status(400).build(); }
        String entryFile = pathValue;
        Files.write(Paths.get("/var/uploads/" + entryFile), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
