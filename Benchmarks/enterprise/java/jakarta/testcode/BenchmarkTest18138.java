// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest18138 {

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest18138")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18138(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String data = normalize(envValue);
        if (data == null) throw new IllegalArgumentException("input required");
        io.github.jopenlibs.vault.VaultConfig vc = new io.github.jopenlibs.vault.VaultConfig()
            .address("https://vault.svc.local:8200")
            .token(System.getenv("VAULT_TOKEN"))
            .build();
        io.github.jopenlibs.vault.Vault vault = io.github.jopenlibs.vault.Vault.create(vc);
        String storeCred = vault.logical().read("secret/myapp/db_password").getData().get("password");
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", storeCred)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
