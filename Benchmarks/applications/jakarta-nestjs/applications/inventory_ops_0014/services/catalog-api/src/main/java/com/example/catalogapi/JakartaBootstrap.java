package com.example.catalogapi;

public class JakartaBootstrap {

    @jakarta.ws.rs.Path("/health")
    public static class HealthResource {
        @jakarta.ws.rs.GET
        public jakarta.ws.rs.core.Response health() {
            return jakarta.ws.rs.core.Response.ok("ok").build();
        }
    }

    public static void main(String[] args) throws Exception {
        java.util.Map<String, String> initParams = new java.util.HashMap<>();
        initParams.put(
            "jersey.config.server.provider.classnames",
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.catalogapi.JakartaBootstrap$HealthResource,com.example.catalogapi.ArchiveHeader,com.example.catalogapi.EnrichHeader,com.example.catalogapi.LoadBatch,com.example.catalogapi.LookupSku,com.example.catalogapi.ReconcileSummary,com.example.catalogapi.RenderLedger,com.example.catalogapi.ResolveAllocation,com.example.catalogapi.RotateDigest,org.glassfish.jersey.media.multipart.MultiPartFeature");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
