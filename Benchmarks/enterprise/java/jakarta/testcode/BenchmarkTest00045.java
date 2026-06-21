// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest00045 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    private static final java.util.concurrent.atomic.AtomicReference<String> sharedRef = new java.util.concurrent.atomic.AtomicReference<>();

    @POST
    @Path("/BenchmarkTest00045/graphql")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00045(GraphQLRequest req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        sharedRef.set(graphqlVar);
        String data = sharedRef.get();
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + data}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
