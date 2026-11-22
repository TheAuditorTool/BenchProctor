import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { SchedulePayout } from "./payout_schedule";
import { FetchMandate } from "./fetch_mandate";
import { PublishReceipt } from "./publish_receipt";
import { RotateConfig } from "./rotate_config";
import { MergeIndex } from "./merge_index";
import { AuditCheckpoint } from "./audit_checkpoint";
import { MergeDigest } from "./merge_digest";
import { CollectManifest } from "./collect_manifest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SchedulePayout, FetchMandate, PublishReceipt, RotateConfig, MergeIndex, AuditCheckpoint, MergeDigest, CollectManifest],
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
