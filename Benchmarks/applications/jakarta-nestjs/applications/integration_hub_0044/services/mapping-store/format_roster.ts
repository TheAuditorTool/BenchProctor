// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("mapping-store")
export class FormatRoster {
  @Post("formatRoster")
  async formatRoster(@Req() req: Request): Promise<unknown> {
    const blurb = (await shared.mq.receive("app-events"));
    const pending: string[] = String(blurb).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const handshake: string = collected.join(',');
    JSON.parse(handshake);
    return { created: true };
  }
}
