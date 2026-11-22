// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.nio.file.Files;
import java.nio.file.Paths;
import javax.ws.rs.container.ContainerRequestContext;
import javax.ws.rs.container.ContainerRequestFilter;
import javax.ws.rs.ext.ExceptionMapper;
import javax.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00237 {

    @Provider
    public static class BindingRestrictionFilter implements ContainerRequestFilter {
        @Override
        public void filter(ContainerRequestContext requestContext) {
            requestContext.getHeaders().remove("X-Internal-Bind");
        }
    }

    @Provider
    public static class FailureMapper implements ExceptionMapper<Exception> {
        @Override
        public Response toResponse(Exception ex) {
            return Response.status(500).entity("request failed").build();
        }
    }

    private static java.sql.Connection connection;
    static {
        try {
            connection = java.sql.DriverManager.getConnection("jdbc:h2:mem:bench;DB_CLOSE_DELAY=-1;NON_KEYWORDS=VALUE", "sa", "");
            try (java.sql.Statement stmt = connection.createStatement()) {
                stmt.execute("CREATE TABLE IF NOT EXISTS profiles (id INTEGER PRIMARY KEY, user_id INTEGER DEFAULT 0 NOT NULL, bio VARCHAR DEFAULT '' NOT NULL)");
                stmt.execute("MERGE INTO profiles t USING (VALUES (1, 1, 'Enjoys hiking'), (2, 2, 'Coffee enthusiast'), (3, 3, 'Site administrator')) s(id, user_id, bio) ON t.id = s.id WHEN NOT MATCHED THEN INSERT (id, user_id, bio) VALUES (s.id, s.user_id, s.bio)");
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
    @Path("/BenchmarkTest00237")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00237(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String profileBio = java.util.Optional.ofNullable(dbReadColumn("SELECT bio FROM profiles LIMIT 1")).orElse("");
        java.nio.file.Path baseName = java.nio.file.Paths.get(profileBio).getFileName();
        String checkedPath = "/var/app/data/" + (baseName == null ? "index" : baseName.toString());
        Files.write(Paths.get(checkedPath), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
