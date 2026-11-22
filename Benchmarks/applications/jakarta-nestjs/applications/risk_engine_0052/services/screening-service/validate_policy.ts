// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("screening-service")
export class ValidatePolicy {
  @Post("validatePolicy")
  async validatePolicy(@Req() req: Request): Promise<unknown> {
    const memo = (req.query.id as string) || "";
    const verdict = Buffer.from(memo, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [verdict]);
    return { created: true };
  }
}
