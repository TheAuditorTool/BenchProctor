// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("catalog-api")
export class ResolveAllocation {
  @Post("resolveAllocation")
  async resolveAllocation(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["x-forwarded-for"] as string) || "";
    const restock = excerpt != null ? excerpt : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(restock)) { throw new BadRequestException({error:"invalid"}); }
    const backorder = restock;
    return "<div>" + backorder + "</div>";
  }
}
