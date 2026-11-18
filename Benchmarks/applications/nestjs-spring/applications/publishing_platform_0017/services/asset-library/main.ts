import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { AttachAsset } from "./asset_attach";
import { CollectSyndication } from "./collect_syndication";
import { FetchBatch } from "./fetch_batch";
import { EnrichConfig } from "./enrich_config";
import { ReconcileWindow } from "./reconcile_window";
import { RenderIndex } from "./render_index";
import { SummarizeLedger } from "./summarize_ledger";
import { ArchiveConfig } from "./archive_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, AttachAsset, CollectSyndication, FetchBatch, EnrichConfig, ReconcileWindow, RenderIndex, SummarizeLedger, ArchiveConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
