// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("escalation-service")
export class AuditHeader {
  @Post("auditHeader")
  async auditHeader(@Req() req: Request): Promise<unknown> {
    const summary = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const _raw = summary;
    const grievance = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(grievance)) { throw new BadRequestException({error:"invalid"}); }
    const inquiry = grievance;
    return "<div>" + inquiry + "</div>";
  }
}
