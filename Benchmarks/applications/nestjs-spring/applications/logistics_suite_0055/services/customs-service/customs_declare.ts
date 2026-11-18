// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("customs-service")
export class DeclareCustoms {
  @Post("declareCustoms")
  async declareCustoms(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers["x-custom-header"] as string) || "";
    const _input = String(heading);
    let consignment;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': consignment = _input.normalize('NFC'); break;
      default: consignment = _input; break;
    }
    await fetch("http://rate-shopper:8080/ShopRate", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
    return { created: true };
  }
}
