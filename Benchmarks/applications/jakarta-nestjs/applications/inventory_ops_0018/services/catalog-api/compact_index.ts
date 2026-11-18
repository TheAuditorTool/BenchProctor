// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("catalog-api")
export class CompactIndex {
  @Post("compactIndex")
  async compactIndex(@Req() req: Request): Promise<unknown> {
    const transcript = (await shared.mq.receive("app-events"));
    const pending: string[] = String(transcript).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const backorder: string = collected.join(',');
    JSON.parse(backorder);
    return { created: true };
  }
}
