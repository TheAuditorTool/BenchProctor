// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest18703 {

    @GET
    @Path("/BenchmarkTest18703")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18703(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String propValue = java.util.Optional.ofNullable(System.getProperty("app.value", "")).orElse("");
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> propValue)
            .thenApply(v -> v.strip().toLowerCase())
            .join();
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
