// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest07556 {

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
    private static boolean authCheck(Object v, Object t) { return v != null && v.equals(t); }

    @POST
    @Path("/BenchmarkTest07556/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest07556(@FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{commentValue});
        if (!authCheck(request.getSession().getAttribute("role"), data)) {
            return Response.status(403).entity("forbidden").build();
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
