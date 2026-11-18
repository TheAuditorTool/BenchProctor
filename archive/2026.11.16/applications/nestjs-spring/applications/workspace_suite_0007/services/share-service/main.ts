import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { GrantShare } from "./share_grant";
import { RenderPolicy } from "./render_policy";
import { PublishRecord } from "./publish_record";
import { LoadRecord } from "./load_record";
import { RenderCheckpoint } from "./render_checkpoint";
import { EnrichDigest } from "./enrich_digest";
import { BuildIndex } from "./build_index";
import { LoadSummary } from "./load_summary";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, GrantShare, RenderPolicy, PublishRecord, LoadRecord, RenderCheckpoint, EnrichDigest, BuildIndex, LoadSummary],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
