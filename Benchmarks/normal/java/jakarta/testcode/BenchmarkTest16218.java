// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest16218 {

    @GET
    @Path("/BenchmarkTest16218")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16218(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "AKIAIOSFODNN7EXAMPLE";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> secretValue)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "))
            .join();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        URL url = java.net.URI.create("https://api.acmecdn.net/v1/data").toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestProperty("Authorization", "Bearer " + processed);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
