import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { QueueRetry } from "./retry_queue";
import { PublishSummary } from "./publish_summary";
import { AuditLedger } from "./audit_ledger";
import { MergeConfig } from "./merge_config";
import { PrunePartner } from "./prune_partner";
import { ValidateConnector } from "./validate_connector";
import { NormalizeCheckpoint } from "./normalize_checkpoint";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, QueueRetry, PublishSummary, AuditLedger, MergeConfig, PrunePartner, ValidateConnector, NormalizeCheckpoint],
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
