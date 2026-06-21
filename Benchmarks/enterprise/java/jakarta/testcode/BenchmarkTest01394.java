// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest01394 {

    @GET
    @Path("/BenchmarkTest01394")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest01394(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "feature_flag_value";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(secretValue, "form");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
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
