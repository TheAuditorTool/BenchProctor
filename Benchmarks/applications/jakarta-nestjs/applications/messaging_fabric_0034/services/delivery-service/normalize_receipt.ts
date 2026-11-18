// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("delivery-service")
export class NormalizeReceipt {
  @Post("normalizeReceipt")
  async normalizeReceipt(@Req() req: Request): Promise<unknown> {
    const footnote = (await shared.mq.receive("app-events"));
    const pending: string[] = String(footnote).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const bulletin: string = collected.join(',');
    JSON.parse(bulletin);
    return { created: true };
  }
}
