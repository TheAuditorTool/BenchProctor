// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;
import javax.net.ssl.*;

@Path("/")
public class BenchmarkTest45766 {

    @GET
    @Path("/BenchmarkTest45766")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest45766(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String prefix = refererValue.length() > 0 ? refererValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = refererValue.toLowerCase(); break;
            case "f": data = refererValue.toUpperCase(); break;
            default: data = refererValue.strip(); break;
        }
        javax.net.ssl.HttpsURLConnection conn = (javax.net.ssl.HttpsURLConnection) java.net.URI.create("https://api.svc.local/data?ref=" + java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8)).toURL().openConnection();
        conn.connect();
        conn.getInputStream().close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
