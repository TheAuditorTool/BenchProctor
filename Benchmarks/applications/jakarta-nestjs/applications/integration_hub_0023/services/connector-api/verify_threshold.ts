// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("connector-api")
export class VerifyThreshold {
  @Post("verifyThreshold")
  async verifyThreshold(@Req() req: Request): Promise<unknown> {
    const caption = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    let handshake;
    try { handshake = JSON.parse(caption).value || ""; }
    catch (e) { handshake = String(caption); }
    nodeSerialize.unserialize(handshake);
    return { created: true };
  }
}
