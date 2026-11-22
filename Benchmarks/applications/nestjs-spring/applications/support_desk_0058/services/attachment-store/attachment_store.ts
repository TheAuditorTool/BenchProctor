// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("attachment-store")
export class StoreAttachment {
  @Post("storeAttachment")
  async storeAttachment(@Req() req: Request): Promise<unknown> {
    const snippet = (req.body?.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(snippet).split(',')) { parts.push(token); }
    const inquiry: string = parts.join(',');
    await fetch("http://escalation-service:8080/RaiseEscalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
    return { created: true };
  }
}
