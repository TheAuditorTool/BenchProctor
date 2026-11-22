import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { UploadDocument } from "./document_upload";
import { AuditBatch } from "./audit_batch";
import { LoadReceipt } from "./load_receipt";
import { ReconcileThreshold } from "./reconcile_threshold";
import { AuditRecord } from "./audit_record";
import { EnrichManifest } from "./enrich_manifest";
import { BuildSignature } from "./build_signature";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, UploadDocument, AuditBatch, LoadReceipt, ReconcileThreshold, AuditRecord, EnrichManifest, BuildSignature],
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
