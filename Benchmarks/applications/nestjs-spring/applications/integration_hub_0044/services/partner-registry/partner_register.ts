// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("partner-registry")
export class RegisterPartner {
  @Post("registerPartner")
  async registerPartner(@Req() req: Request): Promise<unknown> {
    const blurb = (req.body.payload as string) || "";
    const tokens = String(blurb).split(',').filter((t) => t.length > 0);
    const handshake = tokens.join(' ');
    await fetch("http://mapping-store:8080/MapField", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
    return { created: true };
  }
}
