// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest14601 {

    @GET
    @Path("/BenchmarkTest14601/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest14601(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(pathValue);
        String data = normalizer.apply(pathValue);
        return Response.status(500).entity(data).build();
    }
}
