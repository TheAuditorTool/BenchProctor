// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("customs-service")
export class DeclareCustoms {
  @Post("declareCustoms")
  async declareCustoms(@Req() req: Request): Promise<unknown> {
    const caption = (await shared.mq.receive("app-events"));
    const tokens = String(caption).split(',').filter((t) => t.length > 0);
    const parcel = tokens.join(' ');
    await fetch("http://rate-shopper:8080/ShopRate", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
    return { created: true };
  }
}
