// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;
import java.net.*;

@Path("/")
public class BenchmarkTest06271 {

    private static java.sql.Connection connection;
    static {
        try {
            connection = java.sql.DriverManager.getConnection("jdbc:h2:mem:bench;DB_CLOSE_DELAY=-1", "sa", "");
            try (var stmt = connection.createStatement()) {
                stmt.execute("CREATE TABLE IF NOT EXISTS feed (id INT AUTO_INCREMENT, data VARCHAR(2048))");
                stmt.execute("INSERT INTO feed (data) VALUES ('seed-feed')");
            }
        } catch (java.sql.SQLException ignored) {}
    }

    @GET
    @Path("/BenchmarkTest06271")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest06271(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data;
        if (userId.length() > 256) { data = userId.substring(0, 256); }
        else { data = userId; }
        try {
            java.net.http.HttpRequest intReq = java.net.http.HttpRequest.newBuilder(java.net.URI.create(data)).GET().build();
            java.net.http.HttpResponse<byte[]> intResp = java.net.http.HttpClient.newHttpClient().send(intReq, java.net.http.HttpResponse.BodyHandlers.ofByteArray());
            byte[] intDigest = java.security.MessageDigest.getInstance("SHA-256").digest(intResp.body());
            String intHex = java.util.HexFormat.of().formatHex(intDigest);
            if (!intHex.equals(intResp.headers().firstValue("X-Content-SHA256").orElse(""))) { return Response.status(502).entity("integrity").build(); }
            try (java.sql.PreparedStatement ps = connection.prepareStatement("INSERT INTO feed (data) VALUES (?)")) {
                ps.setString(1, new String(intResp.body(), java.nio.charset.StandardCharsets.UTF_8));
                ps.executeUpdate();
            }
        } catch (Exception e) { return Response.status(502).build(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
