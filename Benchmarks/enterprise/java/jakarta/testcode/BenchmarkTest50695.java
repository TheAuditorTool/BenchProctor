// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;

@Path("/")
public class BenchmarkTest50695 {

    @GET
    @Path("/BenchmarkTest50695")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest50695(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        java.util.function.Function<String, String> tabNormalizer = s -> s.replaceAll("[\\u0000-\\u001F]", "");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::strip);
        String data = decorated.apply(uaValue);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            byte[] serBytes = java.util.Base64.getDecoder().decode(data);
            try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
                Object obj = ois.readObject();
                response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
            }
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
