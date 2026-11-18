// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("webhook-receiver")
export class AcceptWebhook {
  @Post("acceptWebhook")
  async acceptWebhook(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["user-agent"] as string) || "";
    const tokens = String(preface).split(',').filter((t) => t.length > 0);
    const handshake = tokens.join(' ');
    await fetch("http://bridge-service:8080/BridgeQueue", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
    return { created: true };
  }
}
