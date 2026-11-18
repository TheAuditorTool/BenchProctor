// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("shipping-api")
export class QuoteShipment {
  @Post("quoteShipment")
  async quoteShipment(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers.origin as string) || "";
    const pending: string[] = String(subject).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const parcel: string = collected.join(',');
    await fetch("http://tracking-service:8080/PollTracking", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
    return { created: true };
  }
}
