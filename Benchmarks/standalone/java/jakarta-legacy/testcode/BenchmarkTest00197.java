// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.validation.Valid;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.container.ContainerRequestContext;
import javax.ws.rs.container.ContainerRequestFilter;
import javax.ws.rs.ext.ExceptionMapper;
import javax.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00197 {
    private static class UserInput {
        @javax.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @Provider
    public static class BindingRestrictionFilter implements ContainerRequestFilter {
        @Override
        public void filter(ContainerRequestContext requestContext) {
            requestContext.getHeaders().remove("X-Internal-Bind");
        }
    }

    @Provider
    public static class FailureMapper implements ExceptionMapper<Exception> {
        @Override
        public Response toResponse(Exception ex) {
            return Response.status(500).entity("request failed").build();
        }
    }

    @POST
    @Path("/BenchmarkTest00197")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00197(@Valid UserInput req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : jsonValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        StringBuilder xmlText = new StringBuilder();
        javax.xml.parsers.SAXParserFactory saxFactory = javax.xml.parsers.SAXParserFactory.newInstance();
        saxFactory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
        javax.xml.parsers.SAXParser saxParser = saxFactory.newSAXParser();
        saxParser.parse(new org.xml.sax.InputSource(new java.io.StringReader(data)), new org.xml.sax.helpers.DefaultHandler() { @Override public void characters(char[] ch, int start, int length) { xmlText.append(ch, start, length); } });
        response.setHeader("X-Xml-Text-Length", String.valueOf(xmlText.length()));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
