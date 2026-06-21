// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest02652 {

    @GET
    @Path("/BenchmarkTest02652")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest02652(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "p4ssw0rd_test_xyz";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(secretValue, "header");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        String hardcodedPassword = "P@ssw0rd_corp_2024";
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", hardcodedPassword)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
