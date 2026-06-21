// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest02052 {

    @GET
    @Path("/BenchmarkTest02052/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest02052(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> pathValue)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "))
            .join();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        byte[] buf = new byte[Integer.parseInt(processed)];
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
