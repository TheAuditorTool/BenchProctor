import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { VerifySignature } from "./signature_verify";
import { ArchiveWebhook } from "./archive_webhook";
import { PublishWindow } from "./publish_window";
import { AuditPartner } from "./audit_partner";
import { AuditBatch } from "./audit_batch";
import { ValidateCheckpoint } from "./validate_checkpoint";
import { SummarizeCheckpoint } from "./summarize_checkpoint";
import { ReconcileRecord } from "./reconcile_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, VerifySignature, ArchiveWebhook, PublishWindow, AuditPartner, AuditBatch, ValidateCheckpoint, SummarizeCheckpoint, ReconcileRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
