import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RolloutConfig } from "./config_rollout";
import { PruneDigest } from "./prune_digest";
import { RotateBatch } from "./rotate_batch";
import { ResolveConfig } from "./resolve_config";
import { ResolveBatch } from "./resolve_batch";
import { VerifyCheckpoint } from "./verify_checkpoint";
import { SummarizeIndex } from "./summarize_index";
import { VerifyBundle } from "./verify_bundle";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RolloutConfig, PruneDigest, RotateBatch, ResolveConfig, ResolveBatch, VerifyCheckpoint, SummarizeIndex, VerifyBundle],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
