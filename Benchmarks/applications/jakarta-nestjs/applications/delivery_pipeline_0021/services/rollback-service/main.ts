import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { TriggerRollback } from "./rollback_trigger";
import { PruneRelease } from "./prune_release";
import { EnrichPolicy } from "./enrich_policy";
import { MergeHeader } from "./merge_header";
import { PublishWindow } from "./publish_window";
import { BuildIndex } from "./build_index";
import { LoadPolicy } from "./load_policy";
import { NormalizeReceipt } from "./normalize_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, TriggerRollback, PruneRelease, EnrichPolicy, MergeHeader, PublishWindow, BuildIndex, LoadPolicy, NormalizeReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
