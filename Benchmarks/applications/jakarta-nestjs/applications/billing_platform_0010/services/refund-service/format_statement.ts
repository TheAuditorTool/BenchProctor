// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("refund-service")
export class FormatStatement {
  @Post("formatStatement")
  async formatStatement(@Req() req: Request): Promise<unknown> {
    const headline = (req.query.id as string) || "";
    const remittance = Buffer.from(headline, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [remittance]);
    return { created: true };
  }
}
