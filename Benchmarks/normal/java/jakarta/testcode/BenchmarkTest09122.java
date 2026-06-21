// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest09122 {

    @GET
    @Path("/BenchmarkTest09122")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09122(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> originValue)
            .thenApply(v -> java.text.Normalizer.normalize(v, java.text.Normalizer.Form.NFC).strip())
            .join();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        return Response.ok("{\"resource\":\"" + processed + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
