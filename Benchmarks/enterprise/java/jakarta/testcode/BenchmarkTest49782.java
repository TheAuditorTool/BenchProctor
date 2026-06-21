// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.sql.*;

@Path("/")
public class BenchmarkTest49782 {

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
    private static final java.util.concurrent.atomic.AtomicReference<String> ref = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest49782")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest49782(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "config_secret_test_abc123";
        ref.set(secretValue);
        String data = ref.get();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        DriverManager.getConnection("jdbc:postgresql://db/prod", "app", processed);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
