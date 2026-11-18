// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("supplier-feed")
export class PublishCheckpoint {
  @Post("publishCheckpoint/:id")
  async publishCheckpoint(@Req() req: Request): Promise<unknown> {
    const citation = (req.params.id as string) || "";
    const backorder = decodeURIComponent(citation);
    if (!/^(asc|desc|name|created)$/.test(String(backorder))) { throw new BadRequestException({error:"invalid"}); }
    const restock = backorder;
    return "<div>" + restock + "</div>";
  }
}
