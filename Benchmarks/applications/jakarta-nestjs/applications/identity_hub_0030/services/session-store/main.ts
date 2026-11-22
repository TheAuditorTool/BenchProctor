import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { CreateSession } from "./session_create";
import { RenderConfig } from "./render_config";
import { ArchiveLedger } from "./archive_ledger";
import { NormalizeThreshold } from "./normalize_threshold";
import { ReconcileRoster } from "./reconcile_roster";
import { AnnotateDevice } from "./annotate_device";
import { SummarizeBatch } from "./summarize_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, CreateSession, RenderConfig, ArchiveLedger, NormalizeThreshold, ReconcileRoster, AnnotateDevice, SummarizeBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
