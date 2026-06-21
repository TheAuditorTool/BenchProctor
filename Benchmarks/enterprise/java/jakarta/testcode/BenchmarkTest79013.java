// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest79013 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @POST
    @Path("/BenchmarkTest79013/graphql")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest79013(GraphQLRequest req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.List<String> tokens = java.util.Arrays.asList(graphqlVar.split(","));
        String data = String.join(",", tokens);
        java.nio.file.Path resolvedBase = java.nio.file.Paths.get("/var/app/data").toAbsolutePath();
        java.nio.file.Path requested = resolvedBase.resolve(data).normalize();
        if (!requested.startsWith(resolvedBase)) { return Response.status(403).entity("outside safe scope").build(); }
        Runtime.getRuntime().exec(new String[]{"chown", "appuser:appgroup", requested.toString()}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        return Response.ok().build();
    }
}
