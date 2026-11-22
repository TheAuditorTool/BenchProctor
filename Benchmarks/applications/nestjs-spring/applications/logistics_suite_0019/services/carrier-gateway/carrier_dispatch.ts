// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("carrier-gateway")
export class DispatchCarrier {
  @Post("dispatchCarrier")
  async dispatchCarrier(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const parcel: string = transform(citation);
    await fetch("http://shipping-api:8080/QuoteShipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
    return { created: true };
  }
}
