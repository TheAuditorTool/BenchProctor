import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { AuthorizePayment } from "./payment_authorize";
import { AnnotateSnapshot } from "./annotate_snapshot";
import { AuditReport } from "./audit_report";
import { SummarizeManifest } from "./summarize_manifest";
import { ValidateConfig } from "./validate_config";
import { PublishPolicy } from "./publish_policy";
import { EnrichWallet } from "./enrich_wallet";
import { MergeDigest } from "./merge_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, AuthorizePayment, AnnotateSnapshot, AuditReport, SummarizeManifest, ValidateConfig, PublishPolicy, EnrichWallet, MergeDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
