// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("allocation-service")
export class ValidateSchedule {
  @Post("validateSchedule")
  async validateSchedule(@Req() req: Request): Promise<unknown> {
    const summary = (await shared.mq.receive("app-events"));
    const pending: string[] = String(summary).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const restock: string = collected.join(',');
    JSON.parse(restock);
    return { created: true };
  }
}
