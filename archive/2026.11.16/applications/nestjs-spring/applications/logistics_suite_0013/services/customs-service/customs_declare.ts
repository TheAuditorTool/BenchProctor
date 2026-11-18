// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { createClient } from "redis";

@Controller("customs-service")
export class DeclareCustoms {
  @Post("declareCustoms")
  async declareCustoms(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const footnote = (await _cache.get("user_data")) || "";
    const parcel = footnote != null ? footnote : '';
    await fetch("http://shipping-api:8080/QuoteShipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
    return { created: true };
  }
}
