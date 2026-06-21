// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest22063 {

    @GET
    @Path("/BenchmarkTest22063")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest22063(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(userId);
        String data = normalizer.apply(userId);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        request.getSession().setAttribute("data", String.valueOf(processed));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
