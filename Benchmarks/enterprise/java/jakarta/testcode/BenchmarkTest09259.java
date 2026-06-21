// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest09259 {

    @GET
    @Path("/BenchmarkTest09259")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09259(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> originValue)
            .thenApply(v -> v.strip().toLowerCase())
            .join();
        if ("admin".equals(data)) {
            return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
        }
        return Response.status(403).entity("forbidden").build();
    }
}
