// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("connector-api")
export class ValidateWebhook {
  @Post("validateWebhook")
  async validateWebhook(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers["user-agent"] as string) || "";
    const pending: string[] = String(snippet).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const handshake: string = collected.join(',');
    net.connect(80, new URL(String(handshake)).hostname);
    return { created: true };
  }
}
