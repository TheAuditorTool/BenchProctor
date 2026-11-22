// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("quota-service")
export class AuditSecret {
  @Post("auditSecret")
  async auditSecret(@Req() req: Request): Promise<unknown> {
    const remark = (req.query.id as string) || "";
    const persona = Buffer.from(remark, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [persona]);
    return { created: true };
  }
}
