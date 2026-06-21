// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest46889 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GET
    @Path("/BenchmarkTest46889")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest46889(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "p4ssw0rd_test_xyz";
        String data = stripCRLF(secretValue);
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
