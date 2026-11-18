import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { UpdateCart } from "./cart_update";
import { CollectPolicy } from "./collect_policy";
import { FormatManifest } from "./format_manifest";
import { ArchiveManifest } from "./archive_manifest";
import { PublishSchedule } from "./publish_schedule";
import { CompactCart } from "./compact_cart";
import { CompactManifest } from "./compact_manifest";
import { ValidateOrder } from "./validate_order";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, UpdateCart, CollectPolicy, FormatManifest, ArchiveManifest, PublishSchedule, CompactCart, CompactManifest, ValidateOrder],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
