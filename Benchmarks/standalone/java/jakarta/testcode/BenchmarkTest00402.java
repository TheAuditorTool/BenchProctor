// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.sql.*;
import jakarta.ws.rs.container.ContainerRequestContext;
import jakarta.ws.rs.container.ContainerRequestFilter;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00402 {

    @Provider
    public static class BindingRestrictionFilter implements ContainerRequestFilter {
        @Override
        public void filter(ContainerRequestContext requestContext) {
            requestContext.getHeaders().remove("X-Internal-Bind");
        }
    }

    @Provider
    public static class FailureMapper implements ExceptionMapper<Exception> {
        @Override
        public Response toResponse(Exception ex) {
            return Response.status(500).entity("request failed").build();
        }
    }

    private static java.sql.Connection connection;
    static {
        try {
            connection = java.sql.DriverManager.getConnection("jdbc:h2:mem:bench;DB_CLOSE_DELAY=-1;NON_KEYWORDS=VALUE", "sa", "");
            try (var stmt = connection.createStatement()) {
                stmt.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR DEFAULT '' NOT NULL, role VARCHAR DEFAULT 'user' NOT NULL, bio VARCHAR DEFAULT '' NOT NULL, email VARCHAR DEFAULT '' NOT NULL, password VARCHAR DEFAULT '' NOT NULL, token_hash VARCHAR DEFAULT '' NOT NULL, locked INTEGER DEFAULT 0 NOT NULL)");
                stmt.execute("MERGE INTO users t USING (VALUES (1, 'alice', 'user', 'Enjoys hiking', 'alice@example.com'), (2, 'bob', 'user', 'Coffee enthusiast', 'bob@example.com'), (3, 'admin', 'admin', 'Site administrator', 'admin@example.com')) s(id, name, role, bio, email) ON t.id = s.id WHEN NOT MATCHED THEN INSERT (id, name, role, bio, email) VALUES (s.id, s.name, s.role, s.bio, s.email)");
            }
        } catch (java.sql.SQLException ignored) {}
    }

    @GET
    @Path("/BenchmarkTest00402")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00402(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("APP_INPUT")).orElse("");
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", envValue);
        String data = sw.toString();
        String sortKey = data.replaceAll("[^a-zA-Z0-9_]", "");
        try (Statement stmt = connection.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT * FROM users ORDER BY " + sortKey)) {
            rs.next();
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
