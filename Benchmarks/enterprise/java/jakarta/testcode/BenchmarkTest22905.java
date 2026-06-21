// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest22905 {

    private static java.sql.Connection connection;
    static {
        try {
            connection = java.sql.DriverManager.getConnection("jdbc:h2:mem:bench;DB_CLOSE_DELAY=-1", "sa", "");
            try (var stmt = connection.createStatement()) {
                stmt.execute("CREATE TABLE IF NOT EXISTS users (id INT, name VARCHAR(64))");
                stmt.execute("INSERT INTO users (id, name) VALUES (1, 'alice')");
                stmt.execute("CREATE TABLE IF NOT EXISTS logs (id INT AUTO_INCREMENT, data VARCHAR(1024))");
                stmt.execute("INSERT INTO logs (data) VALUES ('seed-entry')");
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
    private static boolean authCheck(Object v, Object t) { return v != null && v.equals(t); }

    @GET
    @Path("/BenchmarkTest22905")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest22905(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userName = java.util.Optional.ofNullable(dbReadColumn("SELECT name FROM users LIMIT 1")).orElse("");
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> userName)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        String ownerPrefix = request.getUserPrincipal() != null ? request.getUserPrincipal().getName() + ":" : "anon:";
        if (!data.startsWith(ownerPrefix)) {
            return Response.status(403).entity("forbidden").build();
        }
        return Response.ok("{\"resource\":\"" + data.substring(ownerPrefix.length()) + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
