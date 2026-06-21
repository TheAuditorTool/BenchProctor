// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest04563 {

    @GET
    @Path("/BenchmarkTest04563")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest04563(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "AKIAIOSFODNN7EXAMPLE";
        String data;
        try { data = String.valueOf(Integer.parseInt(secretValue)); }
        catch (NumberFormatException e) { data = secretValue; }
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
