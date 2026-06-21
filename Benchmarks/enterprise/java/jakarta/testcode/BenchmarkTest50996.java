// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.sql.*;

@Path("/")
public class BenchmarkTest50996 {

    private static java.sql.Connection connection;
    static {
        try {
            connection = java.sql.DriverManager.getConnection("jdbc:h2:mem:bench;DB_CLOSE_DELAY=-1", "sa", "");
            try (var stmt = connection.createStatement()) {
                stmt.execute("CREATE TABLE IF NOT EXISTS users (id INT, name VARCHAR(64))");
                stmt.execute("INSERT INTO users (id, name) VALUES (1, 'alice')");
            }
        } catch (java.sql.SQLException ignored) {}
    }

    @GET
    @Path("/BenchmarkTest50996")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest50996(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "default_config_label";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(secretValue, "header");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        if (data == null) throw new IllegalArgumentException("input required");
        java.util.Properties props = new java.util.Properties();
        try (java.io.InputStream propsStream = new java.io.FileInputStream("/etc/app/credentials.properties")) {
            props.load(propsStream);
        }
        String storeCred = props.getProperty("api.key", "");
        String dbPass = System.getenv("DB_PASSWORD");
        DriverManager.getConnection("jdbc:postgresql://db/prod", "app", dbPass);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
