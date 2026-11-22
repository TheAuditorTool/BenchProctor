// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("carrier-gateway")
export class DispatchCarrier {
  @Post("dispatchCarrier")
  async dispatchCarrier(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.authorization as string) || "";
    const _input = String(transcript);
    let consignment;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': consignment = _input.normalize('NFC'); break;
      default: consignment = _input; break;
    }
    await fetch("http://manifest-builder:8080/BuildManifest", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
    return { created: true };
  }
}
