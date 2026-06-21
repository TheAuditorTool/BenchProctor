// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest35037 {

    @GET
    @Path("/BenchmarkTest35037")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest35037(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "config_secret_test_abc123";
        String data = secretValue.isEmpty() ? "default" : secretValue;
        String hardcodedPassword = "P@ssw0rd_corp_2024";
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", hardcodedPassword)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
