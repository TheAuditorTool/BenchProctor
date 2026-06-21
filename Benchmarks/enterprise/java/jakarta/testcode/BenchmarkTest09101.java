// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest09101 {

    @GET
    @Path("/BenchmarkTest09101/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09101(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> pathValue)
            .thenApply(v -> v.replaceAll("[\\x00-\\x1F]", "").strip())
            .join();
        String escaped = "\"" + data.replace("\"", "\"\"") + "\"";
        return Response.ok(escaped + ",data", "text/csv").build();
    }
}
