import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { SettleCapture } from "./capture_settle";
import { BuildThreshold } from "./build_threshold";
import { SummarizeManifest } from "./summarize_manifest";
import { ValidateConfig } from "./validate_config";
import { PublishPolicy } from "./publish_policy";
import { EnrichWallet } from "./enrich_wallet";
import { MergeDigest } from "./merge_digest";
import { SummarizeRecord } from "./summarize_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SettleCapture, BuildThreshold, SummarizeManifest, ValidateConfig, PublishPolicy, EnrichWallet, MergeDigest, SummarizeRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
