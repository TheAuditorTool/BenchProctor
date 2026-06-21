// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest05947 {

    @GET
    @Path("/BenchmarkTest05947")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest05947(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "config_secret_test_abc123";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(secretValue, "query");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
