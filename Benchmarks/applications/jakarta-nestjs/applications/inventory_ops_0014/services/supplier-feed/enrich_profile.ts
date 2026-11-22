// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("supplier-feed")
export class EnrichProfile {
  @Post("enrichProfile")
  async enrichProfile(@Req() req: Request): Promise<unknown> {
    const excerpt = process.env.INVENTORY_INPUT_0014 || "";
    const transform = (v: string): string => v.trim();
    const restock: string = transform(excerpt);
    if (!/^(asc|desc|name|created)$/.test(String(restock))) { throw new BadRequestException({error:"invalid"}); }
    const backorder = restock;
    await db.query("SELECT * FROM users ORDER BY " + backorder);
    return { created: true };
  }
}
