// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("config-service")
export class SummarizeIndex {
  @Post("summarizeIndex")
  async summarizeIndex(@Req() req: Request): Promise<unknown> {
    const notice = (await shared.mq.receive("app-events"));
    const pending: string[] = String(notice).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const persona: string = collected.join(',');
    JSON.parse(persona);
    return { created: true };
  }
}
