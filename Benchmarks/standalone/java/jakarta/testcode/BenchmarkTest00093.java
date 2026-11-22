// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.container.ContainerRequestContext;
import jakarta.ws.rs.container.ContainerRequestFilter;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00093 {

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
            try (var stmt = connection.createStatement()) {
                stmt.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR DEFAULT '' NOT NULL, role VARCHAR DEFAULT 'user' NOT NULL, bio VARCHAR DEFAULT '' NOT NULL, email VARCHAR DEFAULT '' NOT NULL, password VARCHAR DEFAULT '' NOT NULL, token_hash VARCHAR DEFAULT '' NOT NULL, locked INTEGER DEFAULT 0 NOT NULL)");
                stmt.execute("MERGE INTO users t USING (VALUES (1, 'alice', 'user', 'Enjoys hiking', 'alice@example.com'), (2, 'bob', 'user', 'Coffee enthusiast', 'bob@example.com'), (3, 'admin', 'admin', 'Site administrator', 'admin@example.com')) s(id, name, role, bio, email) ON t.id = s.id WHEN NOT MATCHED THEN INSERT (id, name, role, bio, email) VALUES (s.id, s.name, s.role, s.bio, s.email)");
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
    @Path("/BenchmarkTest00093")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00093(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userName = java.util.Optional.ofNullable(dbReadColumn("SELECT name FROM users LIMIT 1")).orElse("");
        java.util.Properties box = new java.util.Properties();
        box.setProperty("value", userName);
        String data = box.getProperty("value", "");
        byte[] dataKey = java.util.Base64.getDecoder().decode(System.getenv("DATA_ENC_KEY"));
        byte[] gcmNonce = new byte[12]; new java.security.SecureRandom().nextBytes(gcmNonce);
        org.bouncycastle.crypto.modes.GCMModeCipher blockMode = org.bouncycastle.crypto.modes.GCMBlockCipher.newInstance(org.bouncycastle.crypto.engines.AESEngine.newInstance());
        blockMode.init(true, new org.bouncycastle.crypto.params.AEADParameters(new org.bouncycastle.crypto.params.KeyParameter(dataKey), 128, gcmNonce));
        byte[] plain = data.getBytes(java.nio.charset.StandardCharsets.UTF_8);
        byte[] sealed = new byte[blockMode.getOutputSize(plain.length)];
        int sealedLen = blockMode.processBytes(plain, 0, plain.length, sealed, 0);
        sealedLen += blockMode.doFinal(sealed, sealedLen);
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(java.util.Arrays.copyOf(sealed, sealedLen)));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
