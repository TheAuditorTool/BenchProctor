// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest10991 {

    @POST
    @Path("/BenchmarkTest10991")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest10991(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.Properties container = new java.util.Properties();
        container.load(new java.io.StringReader("rawValue=" + fieldValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", container.getProperty("format", "plain"));
        String data = container.getProperty("rawValue", "");
        URL url = java.net.URI.create("http://" + data).toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        try {
            conn.connect();
            conn.getInputStream().close();
        } finally { conn.disconnect(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
