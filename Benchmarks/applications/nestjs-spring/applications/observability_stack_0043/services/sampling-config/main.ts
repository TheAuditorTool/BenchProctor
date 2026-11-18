import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ConfigureSample } from "./sample_config";
import { PruneDigest } from "./prune_digest";
import { CompactManifest } from "./compact_manifest";
import { AuditManifest } from "./audit_manifest";
import { PruneAlert } from "./prune_alert";
import { LoadManifest } from "./load_manifest";
import { RenderThreshold } from "./render_threshold";
import { FetchWindow } from "./fetch_window";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ConfigureSample, PruneDigest, CompactManifest, AuditManifest, PruneAlert, LoadManifest, RenderThreshold, FetchWindow],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
