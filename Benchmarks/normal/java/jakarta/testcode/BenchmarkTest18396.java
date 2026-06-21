// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest18396 {

    @GET
    @Path("/BenchmarkTest18396")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18396(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "feature_flag_value";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(secretValue, "header");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        if (data == null) throw new IllegalArgumentException("input required");
        String envSecret = System.getenv("APP_SECRET");
        if (envSecret == null) throw new IllegalStateException("APP_SECRET unset");
        String storeCred = envSecret;
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", storeCred)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
