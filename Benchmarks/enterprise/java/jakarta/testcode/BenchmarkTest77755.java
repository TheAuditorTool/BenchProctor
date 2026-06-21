// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.util.Random;

@Path("/")
public class BenchmarkTest77755 {

    @GET
    @Path("/BenchmarkTest77755")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest77755(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String prefix = authHeader.length() > 0 ? authHeader.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = authHeader.toLowerCase(); break;
            case "f": data = authHeader.toUpperCase(); break;
            default: data = authHeader.strip(); break;
        }
        long seed = ((long) data.hashCode()) & 0xffffffffL;
        int weakRand = new Random(seed).nextInt();
        response.setHeader("X-Rand", String.valueOf(weakRand));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
