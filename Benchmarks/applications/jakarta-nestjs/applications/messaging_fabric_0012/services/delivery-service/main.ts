import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { DispatchDelivery } from "./delivery_dispatch";
import { LoadSubscription } from "./load_subscription";
import { PublishRoster } from "./publish_roster";
import { ArchiveReceipt } from "./archive_receipt";
import { EnrichDelivery } from "./enrich_delivery";
import { ResolveWindow } from "./resolve_window";
import { CompactProfile } from "./compact_profile";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, DispatchDelivery, LoadSubscription, PublishRoster, ArchiveReceipt, EnrichDelivery, ResolveWindow, CompactProfile],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
