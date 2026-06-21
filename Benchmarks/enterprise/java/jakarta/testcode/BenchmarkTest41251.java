// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.util.Random;

@Path("/")
public class BenchmarkTest41251 {

    @GET
    @Path("/BenchmarkTest41251")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest41251(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + refererValue;
        String data = valueSupplier.get();
        long seed = ((long) data.hashCode()) & 0xffffffffL;
        int weakRand = new Random(seed).nextInt();
        response.setHeader("X-Rand", String.valueOf(weakRand));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
