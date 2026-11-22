// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("payment-gateway")
export class CompactPolicy {
  @Post("compactPolicy")
  async compactPolicy(@Req() req: Request): Promise<unknown> {
    const caption = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    let remittance;
    try { remittance = JSON.parse(caption).value || ""; }
    catch (e) { remittance = String(caption); }
    nodeSerialize.unserialize(remittance);
    return { created: true };
  }
}
