import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { UploadAsset } from "./asset_upload";
import { BuildSnapshot } from "./build_snapshot";
import { BuildHeader } from "./build_header";
import { ReconcileAsset } from "./reconcile_asset";
import { VerifyReceipt } from "./verify_receipt";
import { EnrichReceipt } from "./enrich_receipt";
import { PublishProfile } from "./publish_profile";
import { PruneRendition } from "./prune_rendition";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, UploadAsset, BuildSnapshot, BuildHeader, ReconcileAsset, VerifyReceipt, EnrichReceipt, PublishProfile, PruneRendition],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
