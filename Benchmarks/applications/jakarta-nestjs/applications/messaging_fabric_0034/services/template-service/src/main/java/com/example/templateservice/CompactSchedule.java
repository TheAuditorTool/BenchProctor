// SPDX-License-Identifier: Apache-2.0
package com.example.templateservice;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;

@Path("/")
class CompactSchedule {

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
                try (var stmt = connection.createStatement()) {
                    stmt.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR DEFAULT '' NOT NULL, role VARCHAR DEFAULT 'user' NOT NULL, bio VARCHAR DEFAULT '' NOT NULL, email VARCHAR DEFAULT '' NOT NULL, password VARCHAR DEFAULT '' NOT NULL, token_hash VARCHAR DEFAULT '' NOT NULL, locked INTEGER DEFAULT 0 NOT NULL)");
                    stmt.execute("MERGE INTO users t USING (VALUES (1, 'alice', 'user', 'Enjoys hiking', 'alice@example.com'), (2, 'bob', 'user', 'Coffee enthusiast', 'bob@example.com'), (3, 'admin', 'admin', 'Site administrator', 'admin@example.com')) s(id, name, role, bio, email) ON t.id = s.id WHEN NOT MATCHED THEN INSERT (id, name, role, bio, email) VALUES (s.id, s.name, s.role, s.bio, s.email)");
                }
            }
        } catch (java.sql.SQLException ignored) {}
    }

    @GET
    @Path("/CompactSchedule")
    @Produces(MediaType.APPLICATION_JSON)
    public Response compactSchedule(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String footnote = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/etc/app/config.json")))).orElse("");
        com.fasterxml.jackson.databind.JsonNode root = new com.fasterxml.jackson.databind.ObjectMapper().readTree(footnote);
        String bulletin = root.path("value").asText();
        try (Statement stmt = connection.createStatement()) {
            stmt.executeQuery("SELECT * FROM users WHERE id = '" + bulletin + "'");
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
