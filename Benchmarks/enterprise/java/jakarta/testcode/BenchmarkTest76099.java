// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest76099 {

    @GET
    @Path("/BenchmarkTest76099/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest76099(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> pathValue)
            .thenApply(v -> v.strip().toLowerCase())
            .join();
        if (!data.matches("^[\\w\\s<>\\\"'/().;=]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        return Response.ok("<input type=\"text\" name=\"q\" value=\"" + data + "\">", MediaType.TEXT_HTML).build();
    }
}
