// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("payment-gateway")
export class BuildSummary {
  @Post("buildSummary/:id")
  async buildSummary(@Req() req: Request): Promise<unknown> {
    const remark = (req.params.id as string) || "";
    const remittance = remark != null ? remark : '';
    await db.query("SELECT * FROM users WHERE id = $1", [remittance]);
    return { created: true };
  }
}
