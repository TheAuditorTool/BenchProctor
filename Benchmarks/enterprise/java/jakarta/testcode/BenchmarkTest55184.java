// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest55184 {

    @GET
    @Path("/BenchmarkTest55184")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest55184(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String yamlValue = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/etc/app/config.yaml")))).orElse("");
        java.util.List<String> tokens = java.util.Arrays.asList(yamlValue.split(","));
        String data = String.join(",", tokens);
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
