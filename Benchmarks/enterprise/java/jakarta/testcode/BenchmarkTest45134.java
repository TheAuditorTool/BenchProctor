// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest45134 {

    @GET
    @Path("/BenchmarkTest45134")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest45134(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        String prefix = dotenvValue.length() > 0 ? dotenvValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = dotenvValue.toLowerCase(); break;
            case "f": data = dotenvValue.toUpperCase(); break;
            default: data = dotenvValue.strip(); break;
        }
        URL url = java.net.URI.create("http://" + data).toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        try {
            conn.connect();
            conn.getInputStream().close();
        } finally { conn.disconnect(); }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
