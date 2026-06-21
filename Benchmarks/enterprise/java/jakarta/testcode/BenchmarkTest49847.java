// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest49847 {

    @GET
    @Path("/BenchmarkTest49847")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest49847(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "config_secret_test_abc123";
        StringBuilder bundle = new StringBuilder();
        bundle.append(secretValue);
        String data = bundle.toString();
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
