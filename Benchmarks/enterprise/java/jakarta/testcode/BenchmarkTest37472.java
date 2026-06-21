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
public class BenchmarkTest37472 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

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

    @POST
    @Path("/BenchmarkTest37472/graphql")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest37472(GraphQLRequest req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String prefix = graphqlVar.length() > 0 ? graphqlVar.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = graphqlVar.toLowerCase(); break;
            case "f": data = graphqlVar.toUpperCase(); break;
            default: data = graphqlVar.strip(); break;
        }
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
