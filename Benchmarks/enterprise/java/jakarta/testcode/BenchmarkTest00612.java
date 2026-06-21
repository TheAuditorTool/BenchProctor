// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.sql.*;

@Path("/")
public class BenchmarkTest00612 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

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

    @POST
    @Path("/BenchmarkTest00612")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00612(@Valid UserInput req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        java.util.Properties store = new java.util.Properties();
        store.load(new java.io.StringReader("rawValue=" + jsonValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", store.getProperty("format", "plain"));
        String data = store.getProperty("rawValue", "");
        jakarta.persistence.EntityManager em = (jakarta.persistence.EntityManager) request.getAttribute("em");
        if (em == null) { return Response.status(503).entity("no entity manager").build(); }
        em.createQuery("FROM User WHERE name = '" + data + "'", Object.class)
            .getResultList();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
