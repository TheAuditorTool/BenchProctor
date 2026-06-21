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
public class BenchmarkTest31106 {

    @POST
    @Path("/BenchmarkTest31106")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest31106(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String prefix = rawData.length() > 0 ? rawData.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = rawData.toLowerCase(); break;
            case "f": data = rawData.toUpperCase(); break;
            default: data = rawData.strip(); break;
        }
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(data)) { return Response.status(403).build(); }
        String checkedPath = "/var/app/data/" + data;
        java.util.Set<String> allowedExt = java.util.Set.of(".jpg", ".png", ".pdf");
        int dot = checkedPath.lastIndexOf('.');
        String ext = dot >= 0 ? checkedPath.substring(dot).toLowerCase() : "";
        if (!allowedExt.contains(ext)) {
            return Response.status(400).entity("file type not allowed").build();
        }
        Files.write(Paths.get("/var/uploads/" + checkedPath), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
