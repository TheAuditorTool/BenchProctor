// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("platform-api")
export class FetchLedger {
  @Post("fetchLedger")
  async fetchLedger(@Req() req: Request): Promise<unknown> {
    const tagline = (await shared.mq.receive("app-events"));
    const pending: string[] = String(tagline).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const persona: string = collected.join(',');
    JSON.parse(persona);
    return { created: true };
  }
}
