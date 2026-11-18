import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RegisterService } from "./service_register";
import { ResolveIndex } from "./resolve_index";
import { NormalizeRoster } from "./normalize_roster";
import { ArchiveBatch } from "./archive_batch";
import { CollectReceipt } from "./collect_receipt";
import { CompactBundle } from "./compact_bundle";
import { CollectManifest } from "./collect_manifest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RegisterService, ResolveIndex, NormalizeRoster, ArchiveBatch, CollectReceipt, CompactBundle, CollectManifest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
