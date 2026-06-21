// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest03903 {

    @GET
    @Path("/BenchmarkTest03903")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest03903(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "config_secret_test_abc123";
        String data;
        try { data = String.valueOf(Integer.parseInt(secretValue)); }
        catch (NumberFormatException e) { data = secretValue; }
        String hardcodedPassword = "P@ssw0rd_corp_2024";
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", hardcodedPassword)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
