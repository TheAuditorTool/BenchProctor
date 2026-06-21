// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.util.Random;

@Path("/")
public class BenchmarkTest40170 {

    @GET
    @Path("/BenchmarkTest40170")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest40170(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(originValue);
        String data = carrier.toString();
        long seed = ((long) data.hashCode()) & 0xffffffffL;
        int weakRand = new Random(seed).nextInt();
        response.setHeader("X-Rand", String.valueOf(weakRand));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
