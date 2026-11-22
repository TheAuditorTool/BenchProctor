import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { StoreAttachment } from "./attachment_store";
import { NormalizeBatch } from "./normalize_batch";
import { ResolveRecord } from "./resolve_record";
import { FetchBatch } from "./fetch_batch";
import { RenderProfile } from "./render_profile";
import { FetchCheckpoint } from "./fetch_checkpoint";
import { PublishBatch } from "./publish_batch";
import { SummarizeBundle } from "./summarize_bundle";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, StoreAttachment, NormalizeBatch, ResolveRecord, FetchBatch, RenderProfile, FetchCheckpoint, PublishBatch, SummarizeBundle],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
