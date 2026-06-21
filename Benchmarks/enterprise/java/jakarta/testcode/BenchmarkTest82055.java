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
public class BenchmarkTest82055 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @POST
    @Path("/BenchmarkTest82055")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest82055(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = stripCRLF(xmlValue);
        javax.net.ssl.HttpsURLConnection conn = (javax.net.ssl.HttpsURLConnection) java.net.URI.create("https://api.svc.local/data?ref=" + java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8)).toURL().openConnection();
        conn.connect();
        conn.getInputStream().close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
