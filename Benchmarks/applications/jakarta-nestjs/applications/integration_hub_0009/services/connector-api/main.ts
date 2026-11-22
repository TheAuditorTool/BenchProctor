import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { InvokeConnector } from "./connector_invoke";
import { BuildCheckpoint } from "./build_checkpoint";
import { SummarizePolicy } from "./summarize_policy";
import { PublishConfig } from "./publish_config";
import { CollectBundle } from "./collect_bundle";
import { SummarizeRecord } from "./summarize_record";
import { PruneWebhook } from "./prune_webhook";
import { NormalizeRecord } from "./normalize_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, InvokeConnector, BuildCheckpoint, SummarizePolicy, PublishConfig, CollectBundle, SummarizeRecord, PruneWebhook, NormalizeRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
