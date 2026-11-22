import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { TransformPayload } from "./payload_transform";
import { AnnotateSnapshot } from "./annotate_snapshot";
import { NormalizeLedger } from "./normalize_ledger";
import { LoadMapping } from "./load_mapping";
import { RotateCheckpoint } from "./rotate_checkpoint";
import { PublishMapping } from "./publish_mapping";
import { BuildWebhook } from "./build_webhook";
import { CompactCheckpoint } from "./compact_checkpoint";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, TransformPayload, AnnotateSnapshot, NormalizeLedger, LoadMapping, RotateCheckpoint, PublishMapping, BuildWebhook, CompactCheckpoint],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
