// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest10091 {

    @GET
    @Path("/BenchmarkTest10091")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest10091(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> envValue)
            .thenApply(v -> v.replaceAll("[\\x00-\\x1F]", "").strip())
            .join();
        String accessLevel = "none";
        switch (data) {
            case "retry": accessLevel = "scoped-primary"; break;
            case "abort": accessLevel = "scoped-secondary+escalated"; break;
            case "ignore": accessLevel = "scoped-tertiary"; break;
            default: break;
        }
        response.setHeader("X-Access-Level", accessLevel);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
