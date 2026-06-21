// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest36656 {

    @GET
    @Path("/BenchmarkTest36656")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest36656(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "p4ssw0rd_test_xyz";
        String data;
        if (secretValue.length() > 256) { data = secretValue.substring(0, 256); }
        else { data = secretValue; }
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
