// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("customs-service")
export class RenderSummary {
  @Post("renderSummary")
  async renderSummary(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.origin as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(summary);
    const consignment: string = readInput();
    net.connect(80, new URL(String(consignment)).hostname);
    return { created: true };
  }
}
