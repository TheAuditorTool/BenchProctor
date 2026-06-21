// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest77605 {

    @GET
    @Path("/BenchmarkTest77605")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest77605(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        String prefix = dotenvValue.length() > 0 ? dotenvValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = dotenvValue.toLowerCase(); break;
            case "f": data = dotenvValue.toUpperCase(); break;
            default: data = dotenvValue.strip(); break;
        }
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
