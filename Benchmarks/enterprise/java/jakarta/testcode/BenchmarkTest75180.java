// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.sql.*;

@Path("/")
public class BenchmarkTest75180 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }
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

    @GET
    @Path("/BenchmarkTest75180")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest75180(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = toLowerCase(uaValue);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            jakarta.persistence.EntityManager em = (jakarta.persistence.EntityManager) request.getAttribute("em");
            if (em == null) { response.sendError(503, "no entity manager"); return; }
            em.createQuery("FROM User WHERE name = '" + data + "'", Object.class)
                .getResultList();
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
