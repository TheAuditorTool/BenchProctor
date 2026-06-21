// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest44937 {

    @POST
    @Path("/BenchmarkTest44937")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest44937(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String prefix = rawData.length() > 0 ? rawData.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = rawData.toLowerCase(); break;
            case "f": data = rawData.toUpperCase(); break;
            default: data = rawData.strip(); break;
        }
        java.security.MessageDigest md = java.security.MessageDigest.getInstance("SHA-256");
        String hashedCred = java.util.Base64.getEncoder().encodeToString(md.digest(data.getBytes(java.nio.charset.StandardCharsets.UTF_8)));
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", hashedCred)) {
            return Response.ok("{\"auth\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
    }
}
