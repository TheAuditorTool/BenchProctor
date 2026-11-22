// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("cart-service")
export class RenderHeader {
  @Post("renderHeader")
  async renderHeader(@Req() req: Request): Promise<unknown> {
    const headline = (req.query.id as string) || "";
    const backorder = Buffer.from(headline, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [backorder]);
    return { created: true };
  }
}
