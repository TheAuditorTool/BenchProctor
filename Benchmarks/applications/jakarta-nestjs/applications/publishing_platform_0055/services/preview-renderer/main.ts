import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { RenderPreview } from "./preview_render";
import { EnrichBundle } from "./enrich_bundle";
import { BuildSnapshot } from "./build_snapshot";
import { ExportRoster } from "./export_roster";
import { EnrichReport } from "./enrich_report";
import { SummarizeSummary } from "./summarize_summary";
import { AnnotateThreshold } from "./annotate_threshold";
import { RotateCheckpoint } from "./rotate_checkpoint";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RenderPreview, EnrichBundle, BuildSnapshot, ExportRoster, EnrichReport, SummarizeSummary, AnnotateThreshold, RotateCheckpoint],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
