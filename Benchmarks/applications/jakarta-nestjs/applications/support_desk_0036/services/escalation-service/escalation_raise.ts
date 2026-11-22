// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("escalation-service")
export class RaiseEscalation {
  @Post("raiseEscalation")
  async raiseEscalation(@Req() req: Request): Promise<unknown> {
    const quotation = req.body.support_payload || "";
    await db.query("SELECT * FROM users WHERE id = $1", [quotation]);
    return { created: true };
  }
}
