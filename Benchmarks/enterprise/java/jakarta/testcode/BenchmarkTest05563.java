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
public class BenchmarkTest05563 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @POST
    @Path("/BenchmarkTest05563")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest05563(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = stripWhitespace(xmlValue);
        javax.net.ssl.HttpsURLConnection conn = (javax.net.ssl.HttpsURLConnection) java.net.URI.create("https://api.svc.local/data?ref=" + java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8)).toURL().openConnection();
        conn.connect();
        conn.getInputStream().close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
