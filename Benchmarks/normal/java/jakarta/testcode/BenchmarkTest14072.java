// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.security.*;

@Path("/")
public class BenchmarkTest14072 {

    @GET
    @Path("/BenchmarkTest14072")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest14072(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String prefix = uaValue.length() > 0 ? uaValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = uaValue.toLowerCase(); break;
            case "f": data = uaValue.toUpperCase(); break;
            default: data = uaValue.strip(); break;
        }
        byte[] digest = MessageDigest.getInstance("MD5").digest(data.getBytes());
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
