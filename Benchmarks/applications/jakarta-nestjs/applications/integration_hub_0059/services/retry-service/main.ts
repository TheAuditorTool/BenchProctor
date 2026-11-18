import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { QueueRetry } from "./retry_queue";
import { RenderWindow } from "./render_window";
import { EnrichThreshold } from "./enrich_threshold";
import { ExportRoster } from "./export_roster";
import { LoadBundle } from "./load_bundle";
import { MergeConfig } from "./merge_config";
import { AuditBundle } from "./audit_bundle";
import { NormalizeHeader } from "./normalize_header";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, QueueRetry, RenderWindow, EnrichThreshold, ExportRoster, LoadBundle, MergeConfig, AuditBundle, NormalizeHeader],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
