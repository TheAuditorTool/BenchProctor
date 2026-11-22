// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("signature-verifier")
export class ReconcileSummary {
  @Post("reconcileSummary")
  async reconcileSummary(@Req() req: Request): Promise<unknown> {
    const summary = (req.body?.payload as string) || "";
    let handshake;
    try { handshake = JSON.parse(summary).value || summary; }
    catch (e) { handshake = summary; }
    net.connect(80, new URL(String(handshake)).hostname);
    return { created: true };
  }
}
