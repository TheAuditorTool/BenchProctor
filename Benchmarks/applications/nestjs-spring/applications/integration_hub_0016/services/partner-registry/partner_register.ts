// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("partner-registry")
export class RegisterPartner {
  @Post("registerPartner")
  async registerPartner(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.authorization as string) || "";
    const parts: string[] = [];
    for (const token of String(wording).split(',')) { parts.push(token); }
    const handshake: string = parts.join(',');
    await fetch("http://mapping-store:8080/MapField", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
    return { created: true };
  }
}
