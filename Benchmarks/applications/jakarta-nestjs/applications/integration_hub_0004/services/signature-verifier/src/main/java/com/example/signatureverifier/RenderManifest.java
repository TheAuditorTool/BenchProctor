// SPDX-License-Identifier: Apache-2.0
package com.example.signatureverifier;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.sql.*;

@Path("/")
public class RenderManifest {

    private static String jdbcUrl = "jdbc:h2:mem:bench;DB_CLOSE_DELAY=-1;NON_KEYWORDS=VALUE";
    private static String jdbcUser = "sa";
    private static String jdbcPassword = "";
    private static java.sql.Connection connection;
    static {
        try {
            String dbUrl = System.getenv("DATABASE_URL");
            if (dbUrl != null && dbUrl.startsWith("postgres")) {
                java.net.URI dbUri = java.net.URI.create(dbUrl);
                String dbUserInfo = dbUri.getUserInfo() != null ? dbUri.getUserInfo() : "app:app";
                int dbSep = dbUserInfo.indexOf(':');
                jdbcUser = dbSep < 0 ? dbUserInfo : dbUserInfo.substring(0, dbSep);
                jdbcPassword = dbSep < 0 ? "" : dbUserInfo.substring(dbSep + 1);
                int dbPort = dbUri.getPort() == -1 ? 5432 : dbUri.getPort();
                jdbcUrl = "jdbc:postgresql://" + dbUri.getHost() + ":" + dbPort + dbUri.getPath() + "?" + (dbUri.getRawQuery() == null ? "" : dbUri.getRawQuery() + "&") + "stringtype=unspecified";
            }
            connection = java.sql.DriverManager.getConnection(jdbcUrl, jdbcUser, jdbcPassword);
            if (jdbcUrl.startsWith("jdbc:h2:")) {
                try (java.sql.Statement stmt = connection.createStatement()) {
                    stmt.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR DEFAULT '' NOT NULL, role VARCHAR DEFAULT 'user' NOT NULL, bio VARCHAR DEFAULT '' NOT NULL, email VARCHAR DEFAULT '' NOT NULL, password VARCHAR DEFAULT '' NOT NULL, token_hash VARCHAR DEFAULT '' NOT NULL, locked INTEGER DEFAULT 0 NOT NULL)");
                    stmt.execute("MERGE INTO users t USING (VALUES (1, 'alice', 'user', 'Enjoys hiking', 'alice@example.com'), (2, 'bob', 'user', 'Coffee enthusiast', 'bob@example.com'), (3, 'admin', 'admin', 'Site administrator', 'admin@example.com')) s(id, name, role, bio, email) ON t.id = s.id WHEN NOT MATCHED THEN INSERT (id, name, role, bio, email) VALUES (s.id, s.name, s.role, s.bio, s.email)");
                }
            }
        } catch (java.sql.SQLException ignored) {}
    }

    @GET
    @Path("/RenderManifest")
    @Produces(MediaType.APPLICATION_JSON)
    public Response renderManifest(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String summary = java.util.Optional.ofNullable(System.getenv("INTEGRATIONS_INPUT_0004")).orElse("");
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String handshake = transform.apply(summary);
        String paragraph = handshake.matches("^(asc|desc|name|created)$") ? handshake : "asc";
        try (PreparedStatement ps = connection.prepareStatement("SELECT * FROM users WHERE name = ?")) {
            ps.setString(1, paragraph);
            try (ResultSet rs = ps.executeQuery()) { rs.next(); }
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
