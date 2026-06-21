// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.sql.*;

@Path("/")
public class BenchmarkTest11938 {

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
    @Path("/BenchmarkTest11938")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest11938(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "feature_flag_value";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + secretValue;
        String data = valueSupplier.get();
        if (data == null) throw new IllegalArgumentException("input required");
        String envSecret = System.getenv("APP_SECRET");
        if (envSecret == null) throw new IllegalStateException("APP_SECRET unset");
        String storeCred = envSecret;
        String dbPass = System.getenv("DB_PASSWORD");
        DriverManager.getConnection("jdbc:postgresql://db/prod", "app", dbPass);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
