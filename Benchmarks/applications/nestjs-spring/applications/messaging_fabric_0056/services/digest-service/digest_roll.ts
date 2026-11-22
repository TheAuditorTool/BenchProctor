// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("digest-service")
export class RollDigest {
  @Post("rollDigest")
  async rollDigest(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body as string) || "";
    let bulletin;
    try { bulletin = JSON.parse(footnote).value || ""; }
    catch (e) { bulletin = String(footnote); }
    await fetch("http://presence-service:8080/UpdatePresence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
    return { created: true };
  }
}
