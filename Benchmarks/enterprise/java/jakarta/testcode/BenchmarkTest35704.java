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
public class BenchmarkTest35704 {

    @POST
    @Path("/BenchmarkTest35704")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest35704(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(xmlValue)) { return Response.status(403).build(); }
        String checkedPath = "/var/app/data/" + xmlValue;
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
