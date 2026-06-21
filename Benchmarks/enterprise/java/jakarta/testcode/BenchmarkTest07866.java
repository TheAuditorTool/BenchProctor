// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.util.Random;

@Path("/")
public class BenchmarkTest07866 {

    @GET
    @Path("/BenchmarkTest07866")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest07866(@HeaderParam("X-Forwarded-For") String xForwardedFor, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String prefix = forwardedIp.length() > 0 ? forwardedIp.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = forwardedIp.toLowerCase(); break;
            case "f": data = forwardedIp.toUpperCase(); break;
            default: data = forwardedIp.strip(); break;
        }
        long seed = ((long) data.hashCode()) & 0xffffffffL;
        int weakRand = new Random(seed).nextInt();
        response.setHeader("X-Rand", String.valueOf(weakRand));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
