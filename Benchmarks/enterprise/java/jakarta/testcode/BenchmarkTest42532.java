// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest42532 {

    @POST
    @Path("/BenchmarkTest42532")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest42532(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> fieldValue)
            .thenApply(v -> v.length() > 256 ? v.substring(0, 256).strip() : v.strip())
            .join();
        return Response.status(500).entity(data).build();
    }
}
