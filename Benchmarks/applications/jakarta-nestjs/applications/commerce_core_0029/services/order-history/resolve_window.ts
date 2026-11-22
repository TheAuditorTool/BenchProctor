// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("order-history")
export class ResolveWindow {
  @Post("resolveWindow")
  async resolveWindow(@Req() req: Request): Promise<unknown> {
    const notice = (req.body as string) || "";
    const pending: string[] = String(notice).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const backorder: string = collected.join(',');
    nodeSerialize.unserialize(backorder);
    return { created: true };
  }
}
