// SPDX-License-Identifier: Apache-2.0
package com.example.archivestore;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Path("/")
public class StoreArchive {


    @POST
    @Path("/StoreArchive")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response storeArchive(@jakarta.validation.constraints.Size(max = 4096) String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String wording = xmlBody;
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> java.text.Normalizer.normalize(wording, java.text.Normalizer.Form.NFC).strip())
            .thenApply(v -> v.replace("\t", " ").strip());
        String addendum = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        String gateUrl = addendum;
        boolean gateAllowed = false;
        try {
            java.net.URI gateUri = new java.net.URI(gateUrl);
            gateAllowed = ("http".equalsIgnoreCase(gateUri.getScheme()) || "https".equalsIgnoreCase(gateUri.getScheme()))
                    && gateUri.getRawUserInfo() == null
                    && !java.util.regex.Pattern.compile("[\\x00-\\x20\\x7f\\\\]").matcher(gateUrl).find()
                    && gateUri.getHost() != null
                    && java.util.Set.of("api.svc.local", "cdn.acmecdn.net").contains(gateUri.getHost());
        } catch (java.net.URISyntaxException ignored) {
            gateAllowed = false;
        }
        if (!gateAllowed) {
            return Response.status(403).entity("forbidden host").build();
        }
        java.net.HttpURLConnection httpConn = (java.net.HttpURLConnection) java.net.URI.create("http://document-api:3000/document-api/uploadDocument").toURL().openConnection();
        httpConn.setRequestMethod("POST");
        httpConn.setDoOutput(true);
        httpConn.setRequestProperty("Content-Type", "application/json");
        byte[] httpBody = ("{\"documents_payload\": \"" + addendum + "\"}").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        try (java.io.OutputStream httpOut = httpConn.getOutputStream()) { httpOut.write(httpBody); }
        httpConn.getResponseCode();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
