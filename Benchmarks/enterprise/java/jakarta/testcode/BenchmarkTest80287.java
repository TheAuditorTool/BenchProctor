// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.util.Random;

@Path("/")
public class BenchmarkTest80287 {

    @GET
    @Path("/BenchmarkTest80287")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest80287(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String prefix = headerValue.length() > 0 ? headerValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = headerValue.toLowerCase(); break;
            case "f": data = headerValue.toUpperCase(); break;
            default: data = headerValue.strip(); break;
        }
        long seed = ((long) data.hashCode()) & 0xffffffffL;
        int weakRand = new Random(seed).nextInt();
        response.setHeader("X-Rand", String.valueOf(weakRand));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
