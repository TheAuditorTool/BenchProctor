import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { IngestMetric } from "./metric_ingest";
import { ValidateAlert } from "./validate_alert";
import { EnrichReport } from "./enrich_report";
import { BuildThreshold } from "./build_threshold";
import { ArchiveIndex } from "./archive_index";
import { ResolveBundle } from "./resolve_bundle";
import { RenderCheckpoint } from "./render_checkpoint";
import { RotateThreshold } from "./rotate_threshold";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, IngestMetric, ValidateAlert, EnrichReport, BuildThreshold, ArchiveIndex, ResolveBundle, RenderCheckpoint, RotateThreshold],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
