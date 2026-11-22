import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { RenderPreview } from "./preview_render";
import { AuditBatch } from "./audit_batch";
import { ValidateSnapshot } from "./validate_snapshot";
import { CompactRevision } from "./compact_revision";
import { PublishHeader } from "./publish_header";
import { SummarizeSyndication } from "./summarize_syndication";
import { PublishSchedule } from "./publish_schedule";
import { NormalizeBundle } from "./normalize_bundle";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RenderPreview, AuditBatch, ValidateSnapshot, CompactRevision, PublishHeader, SummarizeSyndication, PublishSchedule, NormalizeBundle],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
