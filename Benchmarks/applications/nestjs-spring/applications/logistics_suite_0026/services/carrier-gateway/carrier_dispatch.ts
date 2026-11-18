// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("carrier-gateway")
export class DispatchCarrier {
  @Post("dispatchCarrier")
  async dispatchCarrier(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers["user-agent"] as string) || "";
    const tokens = String(citation).split(',').filter((t) => t.length > 0);
    const parcel = tokens.join(' ');
    await fetch("http://manifest-builder:8080/BuildManifest", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
    return { created: true };
  }
}
