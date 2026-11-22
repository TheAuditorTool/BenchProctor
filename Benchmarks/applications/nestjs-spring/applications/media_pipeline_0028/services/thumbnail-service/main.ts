import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RenderThumbnail } from "./thumbnail_render";
import { MergeReceipt } from "./merge_receipt";
import { NormalizeReceipt } from "./normalize_receipt";
import { CollectPolicy } from "./collect_policy";
import { ResolvePolicy } from "./resolve_policy";
import { CollectRecord } from "./collect_record";
import { RenderAsset } from "./render_asset";
import { PruneCheckpoint } from "./prune_checkpoint";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RenderThumbnail, MergeReceipt, NormalizeReceipt, CollectPolicy, ResolvePolicy, CollectRecord, RenderAsset, PruneCheckpoint],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
