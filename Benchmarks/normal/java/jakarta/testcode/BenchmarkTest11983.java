// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest11983 {

    @GET
    @Path("/BenchmarkTest11983")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest11983(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String propValue = java.util.Optional.ofNullable(System.getProperty("app.value", "")).orElse("");
        String prefix = propValue.length() > 0 ? propValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = propValue.toLowerCase(); break;
            case "f": data = propValue.toUpperCase(); break;
            default: data = propValue.strip(); break;
        }
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
