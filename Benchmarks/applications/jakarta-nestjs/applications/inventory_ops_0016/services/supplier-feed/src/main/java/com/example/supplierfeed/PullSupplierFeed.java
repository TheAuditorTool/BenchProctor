// SPDX-License-Identifier: Apache-2.0
package com.example.supplierfeed;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
class PullSupplierFeed {

    private static String normalize(String v) { return v.strip(); }
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
                    stmt.execute("CREATE TABLE IF NOT EXISTS profiles (id INTEGER PRIMARY KEY, user_id INTEGER DEFAULT 0 NOT NULL, bio VARCHAR DEFAULT '' NOT NULL)");
                    stmt.execute("MERGE INTO profiles t USING (VALUES (1, 1, 'Enjoys hiking'), (2, 2, 'Coffee enthusiast'), (3, 3, 'Site administrator')) s(id, user_id, bio) ON t.id = s.id WHEN NOT MATCHED THEN INSERT (id, user_id, bio) VALUES (s.id, s.user_id, s.bio)");
                }
            }
        } catch (java.sql.SQLException ignored) {}
    }
    private static String dbReadColumn(String sql) {
        try (var stmt = connection.createStatement();
             var rs = stmt.executeQuery(sql)) {
            return rs.next() ? rs.getString(1) : "";
        } catch (java.sql.SQLException e) {
            return "";
        }
    }

    @GET
    @Path("/PullSupplierFeed")
    @Produces(MediaType.APPLICATION_JSON)
    public Response pullSupplierFeed(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String citation = java.util.Optional.ofNullable(dbReadColumn("SELECT bio FROM profiles LIMIT 1")).orElse("");
        String backorder = normalize(citation);
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://catalog-api:3000/catalog-api/lookupSku").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"inventory_payload\": \"" + backorder + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
