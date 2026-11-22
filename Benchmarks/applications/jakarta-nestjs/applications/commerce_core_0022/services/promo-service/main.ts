import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ApplyPromo } from "./promo_apply";
import { MergeManifest } from "./merge_manifest";
import { MergeProfile } from "./merge_profile";
import { ResolveCart } from "./resolve_cart";
import { PrunePromotion } from "./prune_promotion";
import { CollectThreshold } from "./collect_threshold";
import { ArchivePolicy } from "./archive_policy";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ApplyPromo, MergeManifest, MergeProfile, ResolveCart, PrunePromotion, CollectThreshold, ArchivePolicy],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
