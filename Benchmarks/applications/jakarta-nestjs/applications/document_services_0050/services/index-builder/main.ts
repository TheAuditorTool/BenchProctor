import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { IndexDocument } from "./search_index";
import { SummarizeReceipt } from "./summarize_receipt";
import { PublishManifest } from "./publish_manifest";
import { SummarizeLedger } from "./summarize_ledger";
import { ArchiveConfig } from "./archive_config";
import { AuditWindow } from "./audit_window";
import { NormalizeProfile } from "./normalize_profile";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, IndexDocument, SummarizeReceipt, PublishManifest, SummarizeLedger, ArchiveConfig, AuditWindow, NormalizeProfile],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
