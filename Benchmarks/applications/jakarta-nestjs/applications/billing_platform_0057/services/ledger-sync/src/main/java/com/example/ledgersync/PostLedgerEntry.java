// SPDX-License-Identifier: Apache-2.0
package com.example.ledgersync;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Path("/")
public class PostLedgerEntry {

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
                    stmt.execute("CREATE TABLE IF NOT EXISTS mq_messages (id INTEGER PRIMARY KEY, queue VARCHAR DEFAULT '' NOT NULL, body VARCHAR DEFAULT '' NOT NULL)");
                    stmt.execute("MERGE INTO mq_messages t USING (VALUES (1, 'msg-001')) s(id, body) ON t.id = s.id WHEN NOT MATCHED THEN INSERT (id, body) VALUES (s.id, s.body)");
                }
            }
        } catch (java.sql.SQLException ignored) {}
    }
    private static String dbReadColumn(String sql) {
        try (java.sql.Statement stmt = connection.createStatement();
             java.sql.ResultSet rs = stmt.executeQuery(sql)) {
            return rs.next() ? rs.getString(1) : "";
        } catch (java.sql.SQLException e) {
            return "";
        }
    }

    @GET
    @Path("/PostLedgerEntry")
    @Produces(MediaType.APPLICATION_JSON)
    public Response postLedgerEntry(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String caption = java.util.Optional.ofNullable(dbReadColumn("SELECT body FROM mq_messages ORDER BY id DESC LIMIT 1")).orElse("");
        String remittance;
        try { remittance = new String(java.util.Base64.getDecoder().decode(caption), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { remittance = caption; }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://payment-gateway:3000/payment-gateway/capturePayment").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"billing_payload\": \"" + remittance + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
