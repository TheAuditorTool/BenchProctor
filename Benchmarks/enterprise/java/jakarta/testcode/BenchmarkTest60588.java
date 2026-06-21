// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest60588 {

    private static final java.util.concurrent.atomic.AtomicReference<String> ref = new java.util.concurrent.atomic.AtomicReference<>();
    private enum AllowedValue { ACTIVE, PENDING, DELETED, ARCHIVED }

    @GET
    @Path("/BenchmarkTest60588")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest60588(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        ref.set(refererValue);
        String data = ref.get();
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        try (com.mongodb.client.MongoClient mongoClient = com.mongodb.client.MongoClients.create("mongodb://localhost:27017")) {
            com.mongodb.client.MongoCollection<org.bson.Document> mongoUsers = mongoClient.getDatabase("benchmark").getCollection("users");
            org.bson.Document nosqlResult = mongoUsers.find(new org.bson.Document("username", data)).first();
            return Response.ok(nosqlResult != null ? nosqlResult.toJson() : "{}", MediaType.TEXT_HTML).build();
        }
    }
}
