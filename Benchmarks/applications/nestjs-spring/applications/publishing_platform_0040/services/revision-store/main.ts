import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { SaveRevision } from "./revision_save";
import { MergeReceipt } from "./merge_receipt";
import { ResolveManifest } from "./resolve_manifest";
import { EnrichArticle } from "./enrich_article";
import { CompactSnapshot } from "./compact_snapshot";
import { ResolveHeader } from "./resolve_header";
import { RenderRecord } from "./render_record";
import { PruneRevision } from "./prune_revision";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SaveRevision, MergeReceipt, ResolveManifest, EnrichArticle, CompactSnapshot, ResolveHeader, RenderRecord, PruneRevision],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
