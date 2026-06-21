// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16754 {

    @GET
    @Path("/BenchmarkTest16754")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16754(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "s3cr3t_key_test_xyz";
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", secretValue)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
