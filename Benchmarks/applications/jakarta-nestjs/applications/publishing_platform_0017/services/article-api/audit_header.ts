// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("article-api")
export class AuditHeader {
  @Post("auditHeader")
  async auditHeader(@Req() req: Request): Promise<unknown> {
    const summary = (await shared.mq.receive("app-events"));
    const pending: string[] = String(summary).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const addendum: string = collected.join(',');
    JSON.parse(addendum);
    return { created: true };
  }
}
