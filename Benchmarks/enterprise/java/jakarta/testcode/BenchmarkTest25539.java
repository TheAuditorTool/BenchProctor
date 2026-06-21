// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest25539 {

    @GET
    @Path("/BenchmarkTest25539")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest25539(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fileValue = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/var/app/data.txt")))).orElse("");
        String prefix = fileValue.length() > 0 ? fileValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = fileValue.toLowerCase(); break;
            case "f": data = fileValue.toUpperCase(); break;
            default: data = fileValue.strip(); break;
        }
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
