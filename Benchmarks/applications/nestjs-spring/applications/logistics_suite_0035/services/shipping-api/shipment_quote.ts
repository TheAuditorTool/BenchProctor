// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("shipping-api")
export class QuoteShipment {
  @Post("quoteShipment")
  async quoteShipment(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers.referer as string) || "";
    const tokens = String(phrase).split(',').filter((t) => t.length > 0);
    const parcel = tokens.join(' ');
    await fetch("http://customs-service:8080/DeclareCustoms", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
    return { created: true };
  }
}
