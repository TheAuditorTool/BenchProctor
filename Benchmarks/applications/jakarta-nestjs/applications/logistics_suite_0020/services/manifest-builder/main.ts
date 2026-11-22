import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { BuildManifest } from "./manifest_build";
import { MergeHeader } from "./merge_header";
import { VerifyThreshold } from "./verify_threshold";
import { NormalizeBundle } from "./normalize_bundle";
import { PruneManifest } from "./prune_manifest";
import { CompactReceipt } from "./compact_receipt";
import { BuildCheckpoint } from "./build_checkpoint";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, BuildManifest, MergeHeader, VerifyThreshold, NormalizeBundle, PruneManifest, CompactReceipt, BuildCheckpoint],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
