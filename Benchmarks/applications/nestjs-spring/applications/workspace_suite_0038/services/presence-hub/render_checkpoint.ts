// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("presence-hub")
export class RenderCheckpoint {
  @Post("renderCheckpoint/:id")
  async renderCheckpoint(@Req() req: Request): Promise<unknown> {
    const preface = (req.params.id as string) || "";
    const remark = decodeURIComponent(preface);
    if (!/^(asc|desc|name|created)$/.test(String(remark))) { throw new BadRequestException({error:"invalid"}); }
    const wording = remark;
    return "<div>" + wording + "</div>";
  }
}
