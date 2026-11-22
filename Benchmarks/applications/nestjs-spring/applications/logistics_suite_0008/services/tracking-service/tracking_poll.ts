// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("tracking-service")
export class PollTracking {
  @Post("pollTracking")
  async pollTracking(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers["user-agent"] as string) || "";
    let consignment;
    try { consignment = JSON.parse(caption).value || caption; }
    catch (e) { consignment = caption; }
    await fetch("http://shipping-api:8080/QuoteShipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
    return { created: true };
  }
}
