// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("escalation-service")
export class AuditSchedule {
  @Post("auditSchedule")
  async auditSchedule(@Req() req: Request): Promise<unknown> {
    const snippet = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = snippet;
    const inquiry = (_raw && _raw.length > 0) ? _raw : 'default';
    JSON.parse(inquiry);
    return { created: true };
  }
}
