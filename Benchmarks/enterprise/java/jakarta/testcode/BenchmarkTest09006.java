// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest09006 {

    private enum AllowedValue { ACTIVE, PENDING, DELETED, ARCHIVED }

    @GET
    @Path("/BenchmarkTest09006")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09006(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        try { AllowedValue.valueOf(forwardedIp.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { forwardedIp = AllowedValue.values()[0].name().toLowerCase(); }
        try (com.mongodb.client.MongoClient mongoClient = com.mongodb.client.MongoClients.create("mongodb://localhost:27017")) {
            com.mongodb.client.MongoCollection<org.bson.Document> mongoUsers = mongoClient.getDatabase("benchmark").getCollection("users");
            org.bson.Document nosqlResult = mongoUsers.find(new org.bson.Document("username", forwardedIp)).first();
            return Response.ok(nosqlResult != null ? nosqlResult.toJson() : "{}", MediaType.TEXT_HTML).build();
        }
    }
}
