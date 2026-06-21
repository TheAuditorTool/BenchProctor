// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest55240 {

    @GET
    @Path("/BenchmarkTest55240")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest55240(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String secretValue = "default_config_label";
        String data = "" + secretValue;
        if (data == null) throw new IllegalArgumentException("input required");
        java.util.Properties props = new java.util.Properties();
        try (java.io.InputStream propsStream = new java.io.FileInputStream("/etc/app/credentials.properties")) {
            props.load(propsStream);
        }
        String storeCred = props.getProperty("api.key", "");
        URL url = java.net.URI.create("https://api.acmecdn.net/v1/data").toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestProperty("Authorization", "Bearer " + storeCred);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
