import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { IngestMetric } from "./metric_ingest";
import { ArchiveReceipt } from "./archive_receipt";
import { ReconcileSample } from "./reconcile_sample";
import { MergeReport } from "./merge_report";
import { ReconcileSchedule } from "./reconcile_schedule";
import { ResolveWindow } from "./resolve_window";
import { RotateDigest } from "./rotate_digest";
import { MergeReceipt } from "./merge_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, IngestMetric, ArchiveReceipt, ReconcileSample, MergeReport, ReconcileSchedule, ResolveWindow, RotateDigest, MergeReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
