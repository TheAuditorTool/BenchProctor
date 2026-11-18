// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { createClient } from "redis";

@Controller("asset-library")
export class AttachAsset {
  @Post("attachAsset")
  async attachAsset(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const synopsis = (await _cache.get("user_data")) || "";
    const tokens = String(synopsis).split(',').filter((t) => t.length > 0);
    const byline = tokens.join(' ');
    await fetch("http://syndication-feed:8080/PushSyndication", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
    return { created: true };
  }
}
