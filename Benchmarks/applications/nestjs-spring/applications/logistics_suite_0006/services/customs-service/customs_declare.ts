// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("customs-service")
export class DeclareCustoms {
  @Post("declareCustoms")
  async declareCustoms(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    let consignment;
    try { consignment = JSON.parse(summary).value || summary; }
    catch (e) { consignment = summary; }
    await fetch("http://address-validator:8080/ValidateAddress", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
    return { created: true };
  }
}
