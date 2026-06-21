// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest20161 {

    @GET
    @Path("/BenchmarkTest20161")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest20161(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(originValue);
        String data = normalizer.apply(originValue);
        if (!data.matches("^[\\w\\s.\\-:/=\\r\\n]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
