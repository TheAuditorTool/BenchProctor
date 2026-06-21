// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BenchmarkTest20519 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    @POST
    @Path("/BenchmarkTest20519/graphql")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest20519(GraphQLRequest req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(graphqlVar, "request");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        java.util.Set<String> allowed = java.util.Set.of("libapp", "libutils");
        if (!allowed.contains(data)) { return Response.status(403).build(); }
        String checkedPath = data;
        String libName = java.nio.file.Paths.get(checkedPath).getFileName().toString();
        java.util.Set<String> allowedLibs = java.util.Set.of("libapp", "libutils");
        if (!allowedLibs.contains(libName)) {
            return Response.status(403).entity("library not allowed").build();
        }
        System.loadLibrary(libName);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
