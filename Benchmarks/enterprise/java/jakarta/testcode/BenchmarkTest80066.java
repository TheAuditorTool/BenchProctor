// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest80066 {

    @GET
    @Path("/BenchmarkTest80066")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest80066(@Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        java.util.Properties container = new java.util.Properties();
        container.load(new java.io.StringReader("rawValue=" + dotenvValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", container.getProperty("format", "plain"));
        String data = container.getProperty("rawValue", "");
        Cookie cookie = new Cookie("session", data);
        cookie.setMaxAge(86400);
        response.addCookie(cookie);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
