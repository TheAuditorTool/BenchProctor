// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest80235 {

    @GET
    @Path("/BenchmarkTest80235")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest80235(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "default_setting_value";
        String data = String.format("payload=%s", secretValue);
        if (data == null) throw new IllegalArgumentException("input required");
        java.util.Properties props = new java.util.Properties();
        try (java.io.InputStream propsStream = new java.io.FileInputStream("/etc/app/credentials.properties")) {
            props.load(propsStream);
        }
        String storeCred = props.getProperty("api.key", "");
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", storeCred)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
